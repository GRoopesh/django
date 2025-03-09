// Query elements from the DOM
const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');
const hero=document.querySelector(".hero");


// Event listener for register link
registerLink.addEventListener('click', () => {
    wrapper.classList.add('active');
    wrapper.style.display="flex";
    hero.style.display="none";
});

// Event listener for login link
loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active');
    hero.style.display="flex";
        wrapper.style.display="none";
});

// Event listener for login popup button
btnPopup.addEventListener('click', () => {
    wrapper.classList.add('active-popup');
    hero.style.display="none";
        wrapper.style.display="flex";
});

// Event listener for icon close
iconClose.addEventListener('click', () => {
    wrapper.classList.remove('active-popup');
    hero.style.display="flex";
        wrapper.style.display="none";
});


