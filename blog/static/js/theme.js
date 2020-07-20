// changing our logo based on theme
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
    var element = document.body;
    element.classList.toggle("global-hash-dark-version");
    changeLogo()
}