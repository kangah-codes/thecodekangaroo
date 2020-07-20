// changing our logo based on theme
let theme = localStorage.setItem('theme', 'dark')
let changeLogo = () => {
    var element = document.body;
    if (element.classList.contains("global-hash-dark-version")){
        document.getElementById('site-logo').src = "../img/logo-white.png"
    }else{
        document.getElementById('site-logo').src = "../img/logo-dark.png"
    }
}

changeLogo();

function changeTheme() {
    if (localStorage.getItem('theme') == dark){
        localStorage.setItem('theme', 'light')
    }else{
        localStorage.setItem('theme', 'dark')
    }
    var element = document.body;
    element.classList.toggle("global-hash-dark-version");
    changeLogo()
}