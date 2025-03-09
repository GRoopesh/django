// script.js

// Function to show the login form
function showLoginForm() {
    const wrapper = document.querySelector('.wrapper');
    const loginForm = document.querySelector('.form-box.login');
    const registerForm = document.querySelector('.form-box.register');
    wrapper.style.display = 'flex';
    loginForm.style.display = 'block';
    registerForm.style.display = 'none';
}

// Function to show the register form
function showRegisterForm() {
    const wrapper = document.querySelector('.wrapper');
    const loginForm = document.querySelector('.form-box.login');
    const registerForm = document.querySelector('.form-box.register');
    wrapper.style.display = 'flex';
    loginForm.style.display = 'none';
    registerForm.style.display = 'block';
}

// Function to close the login/register form
function closeForm() {
    const wrapper = document.querySelector('.wrapper');
    wrapper.style.display = 'none';
}

// Function to handle login form submission
function login(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    // Perform login logic here
    alert(`Logged in with Email: ${email}`);
}

// Function to handle register form submission
function register(event) {
    event.preventDefault();
    const username = document.getElementById('user').value;
    const email = document.getElementById('mail').value;
    const password = document.getElementById('pass').value;
    
    // Perform registration logic here
    alert(`Registered with Username: ${username}, Email: ${email}`);
}

// Event listeners
document.querySelector('.btnLogin-popup').addEventListener('click', showLoginForm);
document.querySelector('.register-link').addEventListener('click', showRegisterForm);
document.querySelector('.login-link').addEventListener('click', showLoginForm);
document.querySelector('.icon-close').addEventListener('click', closeForm);

document.querySelector('.form-box.login form').addEventListener('submit', login);
document.querySelector('.form-box.register form').addEventListener('submit', register);

