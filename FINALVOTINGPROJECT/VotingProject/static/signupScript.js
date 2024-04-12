document.getElementById('show-password').addEventListener('change', function() {
    let passwordInput1 = document.getElementById('password');
    let passwordInput2 = document.getElementById('confirm-password');
    if (passwordInput1.type === 'password' && passwordInput2.type === 'password') {
        passwordInput1.type = 'text';
        passwordInput2.type = 'text';
    } else {
        passwordInput1.type = 'password';
        passwordInput2.type = 'password';
    }
});

