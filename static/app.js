const lang = document.getElementById('input-lang')
const langIndex = {
    'java': 0,
    'py'  : 1,
    'ml'  : 2,
    'c'   : 3,
    'cpp' : 4
}

function autoLang(evt) {
    const files = evt.target.files
    if (files.length == 0) return
    const file = files[0]
    const l = file.name.split('.')
    lang.selectedIndex = langIndex[l[l.length - 1]]
}

document.getElementById('input-file')
    .addEventListener('change', autoLang, false)
