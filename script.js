// your_app/static/your_app/script.js
document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    if (userInput) {
        addMessage(userInput, 'user');
        document.getElementById('user-input').value = '';
        setTimeout(() => {
            const botResponse = getBotResponse(userInput);
            addMessage(botResponse, 'bot');
        }, 1000);
    }
});

function addMessage(message, sender) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.className = sender === 'user' ? 'user-message' : 'bot-message';
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}

function getBotResponse(input) {
    const lowerInput = input.toLowerCase();

    if (lowerInput.includes('hello') || lowerInput.includes('hi')) {
        return "Hello! How can I assist you today?";
    } else if (lowerInput.includes('how are you')) {
        return "I'm just a program, but thanks for asking! How can I help you?";
    } else if (lowerInput.includes('help')) {
        return "Sure! What do you need help with?";
    } else if (lowerInput.includes('bye')) {
        return "Goodbye! Have a great day!";
    } else if (lowerInput.includes('your name')) {
        return "I'm a chatbot created to assist you!";
    } else if(lowerInput.includes('pain')){
        return "i have a lot of love failure pain!!";
    }
        else {
        return "I'm sorry, I didn't understand that. Can you please rephrase?";
    }
}
document.getElementById('chat-container').classList.add('show');