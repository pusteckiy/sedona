const changeTheme = (theme) => {
    const style = document.documentElement.style
    if (theme == 'dark') {
        document.querySelector('#color-theme-changer').classList.remove('uil-moon')
        document.querySelector('#color-theme-changer').classList.add('uil-sun')
        document.querySelector('#logo').setAttribute('src', logoDark)
        style.setProperty('--body-color', '#101010')
        style.setProperty('--bg-color', '#1E1E1E')
        style.setProperty('--white', '#1E1E1E')
        style.setProperty('--black', '#fff')
        style.setProperty('--gradient', 'linear-gradient(62deg, #FBAB7E 0%, #F7CE68 100%)')
    }
    if (theme == 'white') {
        document.querySelector('#color-theme-changer').classList.remove('uil-sun')
        document.querySelector('#color-theme-changer').classList.add('uil-moon')
        document.querySelector('#logo').setAttribute('src', logo)
        style.setProperty('--body-color', '#f5f5f5')
        style.setProperty('--bg-color', '#fff')
        style.setProperty('--white', '#fff')
        style.setProperty('--black', '#1E1E1E')
        style.setProperty('--gradient', 'linear-gradient(96.00deg, #8EC5FC 0%, #E0C3FC 100%)')
    }
}

const initTheme = () => {
    theme = localStorage.getItem('theme')
    if (theme) {
        changeTheme(theme)
    } else {
        localStorage.setItem('theme', 'white')
    }
}


initTheme()

document.querySelector('#color-theme-changer').addEventListener('click', () => {
    theme = localStorage.getItem('theme')
    if(theme == 'white') {
        localStorage.setItem('theme', 'dark')
    }
    if(theme == 'dark') {
        localStorage.setItem('theme', 'white')
    }
    changeTheme(localStorage.getItem('theme'))
})
