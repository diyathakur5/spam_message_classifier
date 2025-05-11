document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('spam-form');
    const messageInput = document.getElementById('message');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const message = messageInput.value;

        fetch('/predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `<p><strong>Prediction:</strong> ${data.prediction}</p>`;
        })
        .catch(error => {
            resultDiv.innerHTML = `<p>Error: ${error}</p>`;
        });
    });

    // CSRF token function
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
