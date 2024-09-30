document.addEventListener("DOMContentLoaded", function() {
    // Exemplo: evento de clique em um botão
    const button = document.getElementById("myButton");
    button.addEventListener("click", function() {
        alert("Botão clicado!");
    });

    // Exemplo: carregar dados de uma API (pode ser adaptado)
    fetch('/api/dados')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Atualizar o DOM com os dados recebidos
        })
        .catch(error => console.error('Erro:', error));
});
