document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        document.querySelectorAll('.error, .sucesso').forEach(function(alertMessage) {
            alertMessage.style.transition = "opacity 0.5s ease-out"; 
            alertMessage.style.opacity = "0"; 

            setTimeout(() => alertMessage.remove(), 500); 
        });
    }, 5000); 
});