if (document.getElementById("boton")) {
    document.getElementById("boton").addEventListener("click", function () {
        this.setAttribute("disabled", true);
        console.log(form.submit());
    });
}

if(document.getElementById('content')){
    const button = document.getElementById('button');
    button.disabled = true;
}

function validateInput() {
    const input = document.getElementById('content');
    const button = document.getElementById('button');
    if (input.value.length >= 1) {
        button.disabled = false;
    } else {
        button.disabled = true;
    }
}