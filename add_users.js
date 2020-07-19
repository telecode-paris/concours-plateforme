const Promise = require('bluebird');
const sqlite = require('sqlite');
var dbPromise = sqlite.open('database.db', { Promise })
const bcrypt = require('bcrypt-nodejs')

const teams = [ [ 'test',
    '$2a$10$ONxuzpMwtXHFq5RokCADne1Wr.Gf76VrpGQNBrEkv.5R/mJoM7I9e' ],
  [ 'test1',
    '$2a$10$dBr7LGrAgVMPRoLokNvd7OnDdRDSYkafAdklX.7.verwDfPzUNX5K' ],
  [ 'test2',
    '$2a$10$h4nY7k6WhQyOtJV5KHvWOeEa/MhYPWupV9DzkMtFNkOfbKu6hLO4m' ],
  [ 'test3',
    '$2a$10$k0IdmJ8fOt3iW4YOh/DSPO7O785/s5el/cJJsd4Z/gl0yYBbhvv72' ],
  [ 'test4',
    '$2a$10$1EyLaRchqj05uEJ50OiD0e3RkTN0yj35EJJUWeol/AwKbwJFz9RHi' ],
  [ 'test5',
    '$2a$10$1ZFdXIBz4/5k1jg148oI1ezxHKuxKRdDkU5r16UPnaUqFkIs7buvO' ],
  [ 'test6',
    '$2a$10$du1389s1660NZTQMyMHD0uACjnQnR10uRO6Emv7dIqyN4mB0hYcvK' ],
  [ 'test7',
    '$2a$10$QnDnbsGk67gY75ANbSKLKuENlWnMcz8nS.EQosflrCp0wQ2Ro.e16' ],
  [ 'test8',
    '$2a$10$Icmm6HQfYdoYe5xtfQVDo.OTz2GSVCBlZ6RA5c5oEkwKlWt0GOAVK' ],
  [ 'test9',
    '$2a$10$xHwvZKmDOPDBCQebvCJy4e9a8Jh9Sh/lU4JgDm8Ala0fk0B.Y7CDu' ] ]

async function add_team(team) {
    const db = await dbPromise
    db.run(`insert into teams (team_name, team_password)
                      values (?, ?)`,
           team[0], team[1])
        .then(row => {
            console.log("Register team " + team[0] + " to database")
        })
        .catch(err => {
            console.log(err)
        })
}

teams.forEach(add_team)
