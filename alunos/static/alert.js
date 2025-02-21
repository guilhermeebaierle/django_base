// static/js/alert.js
document.addEventListener('DOMContentLoaded', function() {
    var alertMessages = document.querySelectorAll('.alert-message'); // Seleciona todas as mensagens

    alertMessages.forEach(function(alertMessage) {
        // Adiciona funcionalidade ao botão de fechar
        var closeButton = alertMessage.querySelector('.btn-close');
        if (closeButton) {
            closeButton.addEventListener('click', function() {
                alertMessage.remove(); // Remove a mensagem ao clicar no botão de fechar
            });
        }

        // Remove a mensagem após 5 segundos
        setTimeout(function() {
            alertMessage.remove();
        }, 5000); // 5000 milissegundos = 5 segundos
    });
});