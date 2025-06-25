/*
    Файл для взаємодії клієнта з сервером за протоколом WS
*/

const groupId = document.getElementById('groupId').value
const SOCKET_URL = `ws://${window.location.host}/chat/${groupId}`
const CHAT_SOCKET = new WebSocket(SOCKET_URL)

CHAT_SOCKET.addEventListener("open",() => console.log("Успішне з`єднання"))

function processMessageTime(text){
    let date = new Date(text)
    let dateText = date.toLocaleString();
    return dateText
}

const messageTimes = document.querySelectorAll(".message-time")
for (let messageTime of messageTimes){
    let text = messageTime.textContent
    messageTime.textContent = processMessageTime(text)
}

const messages = document.getElementById("messages");
CHAT_SOCKET.addEventListener("message", (event) => {
    let data = JSON.parse(event.data);
    let localTime = processMessageTime(data.datetime)
    messages.innerHTML += `<p>${data.message} (${localTime})</p>`;
})

const messageForm = document.querySelector("#messageForm");
const messageTextInput = document.querySelector("#id_message");
messageForm.addEventListener("submit", (event) => {
    event.preventDefault();
    let message = messageTextInput.value;
    let dataToSend = {"message": message};
    let JSONString = JSON.stringify(dataToSend);
    CHAT_SOCKET.send(JSONString);
    messageForm.reset()
}
)
