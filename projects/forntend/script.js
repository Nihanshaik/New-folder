const chatMessages = document.querySelector('.chat-messages');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', () => {
    const message = messageInput.value;
    if (message.trim() !== '') {
        // Create a new message element
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', 'user-message');
        messageElement.textContent = message;
        chatMessages.appendChild(messageElement);

        // Send the message to ChatGPT (replace with your API call)
        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            const botMessage = document.createElement('div');
            botMessage.classList.add('message', 'bot-message');
            botMessage.textContent = data.response;
            chatMessages.appendChild(botMessage);
        })
        .catch(error => {
            console.error('Error sending message:', error);
        });

        messageInput.value = '';
    }
});