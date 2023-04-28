if (document.getElementById("boton")) {
    document.getElementById("boton").addEventListener("click", function () {
        this.setAttribute("disabled", true);
        this.form.submit();
    });
}