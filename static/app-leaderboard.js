const timeLabel = document.getElementById('time')
const start = new Date(parseInt(document.getElementById('start-input').value))
const deadline = new Date(parseInt(document.getElementById('deadline-input').value))

setInterval(function () {
    let date = Date.now()
    if (deadline < date) {
        timeLabel.classList.remove('primary')
        timeLabel.classList.add('alert')
        timeLabel.innerHTML = "Le concours est terminé"
    } else if (date > start && date < deadline){
        timeLabel.classList.remove('warning')
        timeLabel.classList.add('primary')
        let delta = new Date(deadline - date)
        timeLabel.innerHTML = "Temps restant: " + delta.getUTCHours() + "h " + delta.getUTCMinutes() + "mins " + delta.getUTCSeconds() + "sec "
    } else {
        let delta = new Date(start - date)
        timeLabel.innerHTML = "Le concours n'a pas encore commencé. Il commence dans " + delta.getUTCHours() + "h " + delta.getUTCMinutes() + "mins " + delta.getUTCSeconds() + "sec "
    }
}, 1000)
