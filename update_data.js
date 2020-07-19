const Promise = require('bluebird');
const sqlite = require('sqlite');
var dbPromise = sqlite.open('save/database.db', { Promise })
const bcrypt = require('bcrypt-nodejs')

function valid(id) {
    return !isNaN(parseFloat(id)) && isFinite(id)
}

async function f() {
    if (process.argv.length < 5) {
        console.log("usage: " + process.argv[1] + " <start|deadline> <hours> <min>")
        return
    }

    if (process.argv[2] !== "contest_start" && process.argv[2] !== "contest_deadline") {
        console.log("invalid usage")
        return
    }

    if (!valid(process.argv[3]) || !valid(process.argv[4])) {
        console.log("invalid usage")
        return
    }

    const date = new Date()
    date.setHours(process.argv[3])
    date.setMinutes(process.argv[4])

    const db = await dbPromise
    db.run("update contest_data set " + process.argv[2] + " = ?", date.getTime() / 1000)
        .then(row => {
            console.log("Update " + process.argv[2] + " to " + date)
        })
        .catch(err => {
            console.log(err)
        })
}

f()
