const Promise = require('bluebird');
const sqlite = require('sqlite');
var dbPromise = sqlite.open('save/database.db', { Promise })
const bcrypt = require('bcrypt-nodejs')

async function f() {
    if (process.argv.length < 4) {
        console.log("usage: " + process.argv[1] + " <team_name> <team_password>")
        return
    }

    user = process.argv[2]
    pass = process.argv[3]
    const db = await dbPromise
    db.run(`insert into teams (team_name, team_password)
                      values (?, ?)`,
           user, bcrypt.hashSync(pass))
        .then(row => {
            console.log("Register team " + user + " to database")
        })
        .catch(err => {
            console.log(err)
        })
}

f()
