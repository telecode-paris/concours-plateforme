const express = require('express')
const port = process.env.PORT ? parseInt(process.env.PORT) : 8080;

const Promise = require('bluebird');
const sqlite = require('sqlite');
var dbPromise = sqlite.open('save/database.db', { Promise })

const { check, validationResult } = require('express-validator/check');

const multer = require('multer')
const upload = multer({ dest: 'save/uploads/' })

const path = require('path')
const fs = require('fs')
const request = require('request')
const bodyParser = require('body-parser')

const uuid = require('uuid/v4')
const session = require('express-session')
const passport = require('passport')
const LocalStrategy = require('passport-local').Strategy
const bcrypt = require('bcrypt-nodejs')

const OK = 0
const FAILED = 1
const COMPILE_ERROR = 2
const RUNTIME_ERROR = 3
const TIMED_OUT = 4
const OUT_OF_MEMORY = 5

const STATUS = {
    'OK' : OK,
    'FAILED' : FAILED,
    'COMPILE_ERROR' : COMPILE_ERROR,
    'RUNTIME_ERROR' : RUNTIME_ERROR,
    'TIMED_OUT' : TIMED_OUT,
    'OUT_OF_MEMORY' : OUT_OF_MEMORY,
}

const INFO = 0
const WARN = 1
const ERR = 2

function log(level, log) {
    const date = new Date().toLocaleString()
    const l = level == INFO ? "info" : level == WARN ? "warning" : "error"
    console.log("[" + l + ": " + date + "]: " + log)
}

passport.use(new LocalStrategy(
    { usernameField: 'team' },
    async (team_name, password, done) => {
        const db = await dbPromise
        const team = await
        db.get(`select team_id, team_name, team_password
                from teams where team_name = ?`, team_name)

        if (!team || !bcrypt.compareSync(password, team.team_password))
            return done(null, false, {message : 'Nom d\'équipe ou mot de passe invalide.'})
        return done(null, team)
    }
))

passport.serializeUser((team, done) => {
    return done(null, team.team_id)
})

passport.deserializeUser(async (id, done) => {
    const db = await dbPromise
    const team = await
    db.get(`select team_id, team_name, team_password
                    from teams where team_id = ?`, id)

    return done(null, team)
})

const app = express()

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(express.static('static'))
app.set('views', './views')
app.set('view engine', 'pug')

app.use(session({
    genid: (req, res) => uuid(),
    secret: uuid(),
    resave: false,
    saveUninitialized: true
}))

app.use(passport.initialize());
app.use(passport.session());

const team_field_checks = [
    check('team').not().isEmpty().trim().escape().withMessage('No team name'),
    check('password').trim().escape().not().isEmpty().withMessage('No password'),
]

app.get('/', async (req, res) => {
    if (req.isAuthenticated()) return res.redirect('/dashboard')

    const db = await dbPromise
    const data = await
    db.get(`select contest_start as start,
            contest_deadline as deadline
            from contest_data`)


    res.render('index', {
        title:'Homepage',
        text:'Bienvenue !',
        connected:req.isAuthenticated(),
        data
    })
})

app.get('/info', async (req, res) => {
    const db = await dbPromise
    const data = await
    db.get(`select contest_start as start,
            contest_deadline as deadline
            from contest_data`)

    res.render('info', {
        title: 'Informations',
        connected: req.isAuthenticated(),
        data
    })
})

app.get('/dashboard', async (req, res) => {
    const db = await dbPromise
    const [problems, data] = await Promise.all([
        db.all(`select problem_id, problem_name,
                problem_difficulty
                from problems order by problem_difficulty asc`),
        db.get(`select contest_start as start,
            contest_deadline as deadline
            from contest_data`)])

    res.render('dashboard', {
        title:'All Problems',
        connected: req.isAuthenticated(),
        problems,
        data
    })
})

app.get('/leaderboard', async (req, res) => {
    const db = await dbPromise
    const [teams, data] = await Promise.all([
        db.all(`select sum(test_points) as points, team_name,
                sum(julianday(submission_date) - julianday(datetime('?'))) as times,
                sum(execution_time) as full_execution_time
                from teams
                natural join tests
                natural join submissions
                where status = 0
                group by team_name
                having points > 0
                order by points desc, times asc, full_execution_time asc
                limit 100`),
        db.get(`select contest_start as start,
            contest_deadline as deadline
            from contest_data`)])

    res.render('leaderboard', {
        title:'Leaderboard',
        connected: req.isAuthenticated(),
        teams,
        data
    })
})

const requestConnected =
      `select test_id, test_points,
       submission_date, execution_time,
       status, test_time
       from (
        select test_id, test_points,
        submission_date, execution_time,
        status, test_time
        from submissions
        natural join tests
        where problem_id = ?
              and team_id = ?
        union
        select test_id, test_points,
        null, null, null, test_time
        from tests
        where test_id not in
             (select test_id from submissions
             where team_id = ?)
             and problem_id = ?)`

const requestNotConnected =
      `select test_id, test_points, test_time from tests where problem_id = ?`

function validId(id) {
    return !isNaN(parseFloat(id)) && isFinite(id)
}

async function showProblems (req, res, errors) {
    if (!validId(req.params.id)) return res.redirect('/dashboard')
    const db = await dbPromise
    queries = [
        req.isAuthenticated() ?
            db.all(requestConnected, req.params.id,
                   req.session.passport.user, req.session.passport.user,
                   req.params.id) :
            db.all(requestNotConnected, req.params.id),
        db.get(`select problem_id, problem_name,
                problem_difficulty, problem_description
                from problems
                where problem_id = ?`, req.params.id),
        db.get(`select contest_start as start,
            contest_deadline as deadline
            from contest_data`)
    ]

    const [tests, prob, data] = await Promise.all(queries)
    if (!prob) return res.redirect('/dashboard')

    if (data.start * 1000 > Date.now()) {
        log(WARN, "Acces problem before start")
    }

    return res.render('problem', {
        title:'Problem ' + req.params.id,
        connected: req.isAuthenticated(),
        prob,
        tests,
        errors: errors,
        data
    })
}

async function insertSubmission (test_id, team_id, st, exec_time) {
    const db = await dbPromise
    const row = await db.get(`select status, execution_time from submissions
                              where test_id = ? and team_id = ?`,
                             test_id, team_id)
    if (row && (row.status != 0 || (row.status == 0 && row.execution_time > exec_time))) {
        log(INFO, "update submission of team " + team_id + " for test " + test_id + " with status " + st + " and execution time " + exec_time)
        db.run(`update submissions
                     set status = ?, submission_date = CURRENT_TIMESTAMP,
                     execution_time = ? where test_id = ? and team_id = ?`,
               st, exec_time, test_id, team_id)
    } else if (!row) {
        log(INFO, "insert new submission for team " + team_id + " for test " + test_id + " with status " + st + " and execution time " + exec_time)
        db.run(`insert into submissions (test_id, team_id, status, execution_time)
                     values (?, ?, ?, ?)`, test_id, team_id, st, exec_time)
    }
}

app.get('/problem/:id', showProblems)

app.post('/problem/:id', upload.single('file'), [
    check('code').custom((value, { req }) => {
        if (!req.file) {
            log(WARN, "team " + req.session.passport.user + " submitted no file.")
            throw new Error("Vous avez oublié de soumettre un fichier.")
        }

        const ext = path.extname(req.file.originalname)
        if (['.ml', '.c', '.java', '.py', '.cpp'].indexOf(ext) < 0) {
            log(WARN, "team " + req.session.passport.user + " submitted file " + req.file.originalname + ", unvalid language.")
            throw new Error('Fichier non valide.')
        }

        const code = fs.readFileSync(req.file.path, 'utf-8')
        if (!code) {
            log(WARN, "Team " + req.session.passport.user + " submitted an empty file.")
            throw new Error('Fichier vide.')
        }

        return code
    }),
    check('lang').custom((value, { req }) => {
        if (['ocaml', 'c', 'java', 'python', 'c++'].indexOf(value) < 0) {
            log(WARN, "Team " + req.session.passport.user + " choosed an unvalid language " + value)
            throw new Error('Langage non supporté.')
        }

        return value
    })
], async (req, res) => {
    if (!req.isAuthenticated() || !validId(req.params.id))
        return res.redirect('/dashboard')

    const errors = validationResult(req)
    if (!errors.isEmpty()) {
        log(WARN, "Team " + req.session.passport.iser + " has submitted an unvalid form")
        return showProblems(req, res, errors.mapped())
    }

    const db = await dbPromise
    const data = await
    db.get(`select contest_start as start,
            contest_deadline as deadline
            from contest_data`)

    if (data.start * 1000 > Date.now()) {
        log(WARN, "Team " + req.session.passport.user + " submitted file before start")
        return res.redirect('/')
    }

    if (data.deadline * 1000 - Date.now() < 0) {
        log(WARN, "Team " + req.session.passport.user + " submitted file after deadline")
        return showProblems(req, res, {})
    }

    // TODO: dont re-read file content
    var code = fs.readFileSync(req.file.path, 'utf-8')

    log(INFO, "Team " + req.session.passport.user + " submitted file " + req.file.path + " for problem " + req.params.id)

    const full_tests = await
    db.all(`select test_id as name, test_time as time,
                test_in as stdin, test_out as stdout
                from tests
                where problem_id = ?`, req.params.id)

    if (!full_tests) {
        log(ERR, "No test founded for problem " + req.params.id)
        return res.redirect('/dashboard')
    }

    const tests = full_tests.map(test => {return {
        name: '' + test.name,
        stdin: test.stdin + '\n',
        'wall-time': test.time
    }})

    request({
        uri: 'http://localhost:9000/run',
        method: 'post',
        json: {
            lang: req.body.lang,
            source: code, // TODO : bug if file is empty
            execute: {
                'wall-time': 120,
                processes: 1,
                mem: 500000,
            },
            tests
        }
    }, (err, res, body) => {
        if (err) {
            log(ERR, "Error on response from camisole")
            return log(ERR, err)
        }

        if (!body.success) {
            log(ERR, "Error from camisole")
            return log(ERR, body)
        }

        if (body.compile && body.compile.exitcode != 0 ||
            body.execute && body.execute.exitcode != 0) {
            status = body.compile ? COMPILE_ERROR : RUNTIME_ERROR
            log(WARN, "Error on submission of team " + req.session.passport.user + " for problem " + req.params.id + " with status " + status)
            for (var i = 0; i < full_tests.length; i++) {
                insertSubmission(full_tests[i].name,
                                 req.session.passport.user, status)
            }
            return
        }

        for (var i = 0; i < body.tests.length; i++) {
            const st = body.tests[i].exitcode != 0 ?
                  STATUS[body.tests[i].meta.status] :
                  body.tests[i].stdout.trim() == full_tests[i].stdout.trim() ?
                  OK : FAILED
            log(INFO, "Problem " + req.params.id + " submission from team " + req.session.passport.user)
            log(INFO, "test #" + i + ": " + st)
            insertSubmission(
                parseInt(body.tests[i].name),
                req.session.passport.user, st,
                body.tests[i].meta['wall-time'])
            if (st != OK) break;
        }
    })

    res.redirect('/problem/' + req.params.id)
})

// TODO: proper render
app.get('/login', (req, res) => res.redirect('/'))
app.get('/register', (req, res) => res.redirect('/'))

app.post('/login', team_field_checks, (req, res, next) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.render('index', {
            title: 'Accueil',
            connected: false,
            loginErrors: errors.mapped()
        })
    }

    passport.authenticate('local', (err, team, info) => {
        if (info) return res.render('index', {
            title:'Accueil',
            text:'Binvenue !',
            alert: info.message,
            connected:req.isAuthenticated()
        })

        if (err) return next(err)
        if (!team) return res.redirect('/')
        req.login(team, err => {
            if (err) return next(err)
            return res.redirect('/dashboard')
        })
    })(req, res, next)
})

app.get('/logout', (req, res) => {
    req.logout()
    return res.render('index', {title:'Accueil', text: 'À bientôt !'})
})

app.listen(port, () => console.log(`Run server on ${port}.`))
