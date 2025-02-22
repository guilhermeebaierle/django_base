document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        document.querySelectorAll('.alert-message').forEach(function(alertMessage) {
            alertMessage.style.transition = "opacity 0.5s ease-out"; // Transição suave
            alertMessage.style.opacity = "0"; // Começa a desaparecer

            setTimeout(() => alertMessage.remove(), 500); // Remove após o fade-out
        });
    }, 5000); // 5 segundos
});