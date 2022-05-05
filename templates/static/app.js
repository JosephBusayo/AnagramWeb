const menu = document.querySelector('#mobileMenu');
const menuliinks = document.querySelector('.nav-menu');

menu.addEventListener('click', function () {
  menu.classList.toggle('is-active');
  menuliinks.classList.toggle('active');
});
