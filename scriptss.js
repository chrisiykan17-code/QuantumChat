// Wait for the page to load document.addEventListener(
'DOMContentLoaded', () =>
{
    const generateBtn =
    document.getElementById('generateBtn');

    //listen for click

    generateBtn.addEventListener('click', generateKey);

}
async function generateKey() {
    const chatBox = 
    document.getElementById('chatBox') 

    //1. Show user Message (Right Side)

    chatBox.innerHTML += `
    <div class="message outgoing"> Requesting Key...</div>`;

    // Auto scroll to bottom
    chatBox.scrollTop =
    chatBox.scrollHeight;

    try {
        // 2. call python backend
        const response = await
        fetch('http://127.0.0.1:5000/get-key');
        const data = await
        response.json();
        
        // 3. show Quantum Response(Left Side)
        
        chatBox.innerHTML += `
        <div class="message incoming"> <strong>Sucess.</strong><br>
        key: <span class="key-text">${data.quantum_key}</span></div>
        <div class="clear"> </div>`;
    }
    catch (error) {
        // Error handling
        chatBox.innerHTML += `
        <div class="message incoming" style="border:1px solid red;">
        Error: Is app.py running?</div>
        <div class="clear"></div>`;
    }
    // Auto scroll to bottom again 
    chat.Box.scrollTop =
    chatBox.scrollHeight;
}

