function consult_user() {
    let id = document.getElementById("id").value;

    if (!id) {
        alert("Por favor, ingresa un ID válido.");
        return;
    }

    fetch("/consult_user", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: id })
    })
    .then(resp => {
        if (resp.ok) {
            alert("DATOS ENVIADOS");
        } else {
            alert("ERROR EN LA CONSULTA"+ resp);
        }
    })
    .then(data => document.getElementById("txt-area").value = data.name + " " + data.last_name)
    .catch(e => {
        console.log("Hola, mundo de errores!", e);
        alert("ERROR CON: " + e);
    });
}
