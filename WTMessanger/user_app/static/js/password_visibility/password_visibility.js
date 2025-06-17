let passwordInput = document.getElementById("id_password");
let passwordConfInput = document.getElementById("id_password2");

let togglePassword = document.getElementById("eye-icon");
let togglePasswordConf = document.getElementById("eye-icon-conf");

togglePassword.addEventListener("click", function () {
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        togglePassword.src = "/static/images/opened-eye.svg"; 

        console.log("Password visibility toggled to text");
    } else {
        passwordInput.type = "password";
        togglePassword.src = "/static/images/closed_eye.svg"; 

        console.log("Password visibility toggled to password");
    }
});

togglePasswordConf.addEventListener("click", function () {
    if (passwordConfInput.type === "password"){
        passwordConfInput.type = "text";
        togglePasswordConf.src = "/static/images/opened-eye.svg"; 
        console.log("Password confirmation visibility toggled to text");
    } else {
        passwordConfInput.type = "password";
        togglePasswordConf.src = "/static/images/closed_eye.svg"; 
    }
});