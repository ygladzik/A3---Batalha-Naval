const form = document.getElementById("form");
const userInput = document.getElementById("user");
const passwordInput = document.getElementById("password");
const password_confInput = document.getElementById("password_conf");

form.addEventListener("submit", (event) => {
    event.preventDefault();

    //Verifica se o user está vazio

    if(userInput.value === ""){
        alert("Por favor, preencha o seu usuário");
        return;
    }
    //Verifica se a está preenchida
    if(!validatePassword(passwordInput.value, 6)){
        alert("A senha precisa de no mínimo 6 dígitos");
        return;
    }
    // Verifica se a senha e a confirmação de senha são idênticas
    if (passwordInput.value !== password_confInput.value) {
        alert("A senha e a confirmação de senha não coincidem. Por favor, tente novamente.");
        return;
    }
    // Se todos os campos estiverem corretamente preenchidos, envie o form
    form.submit();
});

//função que valida a senha
function validatePassword(password, MinDigits) {
    if(password.length >= MinDigits){
        //Válida
        return true;
    }
    return false;
}
