var homeColor
var aboutColor
if (window.location.href == 'http://localhost:8000/' || window.location.href == 'http://127.0.0.1:8000/') {
    homeColor = 'green';
    aboutColor = '';
}else if (window.location.href == 'http://localhost:8000/about/' || window.location.href == 'http://127.0.0.1:8000/about/') {
    aboutColor = 'green';
    homeColor = ''
}
document.getElementById('home').style.backgroundColor = homeColor;
document.getElementById('about').style.backgroundColor = aboutColor;