// changing our logo based on theme
if (localStorage.getItem('theme') == null){
    let theme = localStorage.setItem('theme', 'dark')
}

$(window).on('load', function () {
    $('#preloader').fadeOut('1000', function () {
        $(this).remove();
    });
});
var newsletter = ["Start your day with <thecodekangaroo/>", "No spam ever, we promise!", "Get notified when we post"]
var subscribe = document.getElementById("subscribe");
if (subscribe) {
    ityped.init(document.querySelector(".ityped-wrap"), {
        strings: newsletter,
        showCursor: true,
        typeSpeed: 150,
        startDelay: 500,
        backDelay: 5000,
    });
}

function changeLogo(){
    var imgs = document.getElementsByClassName('site-logo')
    console.log(imgs.length)
    var element = document.body;
    if (element.classList.contains("global-hash-dark-version")){
        for (let i=0;i<imgs.length;i++){
            imgs[i].src = "http://"+window.location.hostname+"/static/img/logo-white.png"
        }
        
    }else{
        for (let i=0;i<imgs.length;i++){
            imgs[i].src = "http://"+window.location.hostname+"/static/img/logo-dark.png"
        }
    }
}



function changeTheme() {
    var element = document.body;
    var imgs = document.getElementsByClassName('site-logo')
    
    if (localStorage.getItem('theme') == 'dark'){
        localStorage.setItem('theme', 'light')
        element.classList.remove("global-hash-dark-version");
    }else{
        localStorage.setItem('theme', 'dark')
        element.classList.add("global-hash-dark-version");
    }
    changeLogo()
}

window.onload = () => {
    var element = document.body;
    if (localStorage.getItem('theme') == 'dark'){
        element.classList.add("global-hash-dark-version");
        changeLogo()
    }else{
        element.classList.remove("global-hash-dark-version");
    }
}