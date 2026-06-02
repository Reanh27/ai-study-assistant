function showTyping() {

    const chatBox = document.getElementById("chat-box");

    const typingDiv = document.createElement("div");

    typingDiv.className = "bot-message";

    typingDiv.id = "typing-indicator";

    typingDiv.innerHTML = `
        <div class="message-content">
            <div class="typing">
             <span></span>
             <span></span>
             <span></span>
             </div>
        </div>
    `;

    chatBox.appendChild(typingDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTyping() {

    const typing = document.getElementById("typing-indicator");

    if (typing) {
        typing.remove();
    }
}

// =========================
// AETHER AI SCRIPT
// =========================

const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");

// =========================
// SEND MESSAGE
// =========================

async function sendMessage() {

    const message = userInput.value.trim();

    if (message === "") {
        return;
    }

    addUserMessage(message);

    userInput.value = "";

    try {

        showTyping();

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        removeTyping();

        addBotMessage(data.reply);

    } catch (error) {

        addBotMessage(
            "⚠ Unable to connect to Aether AI."
        );

        console.error(error);
    }
}

// =========================
// USER MESSAGE
// =========================

function addUserMessage(text) {

    const messageDiv = document.createElement("div");

    messageDiv.className = "user-message";

    messageDiv.innerHTML = `
        <div class="message-content">
            ${escapeHtml(text)}
        </div>
    `;

    chatBox.appendChild(messageDiv);

    scrollToBottom();
}

// =========================
// BOT MESSAGE
// =========================

function addBotMessage(text) {

    const messageDiv = document.createElement("div");

    messageDiv.className = "bot-message";

    messageDiv.innerHTML = `
        <div class="message-content">
            ${escapeHtml(text)}
        </div>
    `;

    chatBox.appendChild(messageDiv);

    scrollToBottom();
}

// =========================
// AUTO SCROLL
// =========================

function scrollToBottom() {

    chatBox.scrollTop =
        chatBox.scrollHeight;
}

// =========================
// ENTER KEY SUPPORT
// =========================

userInput.addEventListener(
    "keypress",
    function (event) {

        if (event.key === "Enter") {

            event.preventDefault();

            sendMessage();
        }
    }
);

// =========================
// VOICE RECOGNITION
// =========================

function startVoiceRecognition() {

    const SpeechRecognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;

    if (!SpeechRecognition) {

        alert(
            "Speech recognition is not supported in this browser."
        );

        return;
    }

    const recognition =
        new SpeechRecognition();

    recognition.lang = "en-US";

    recognition.interimResults = false;

    recognition.maxAlternatives = 1;

    recognition.start();

    const voiceBtn =
        document.getElementById("voice-btn");

    voiceBtn.innerText = "🎙";

    recognition.onresult = function (event) {

        const transcript =
            event.results[0][0].transcript;

        userInput.value = transcript;

        voiceBtn.innerText = "🎤";
    };

    recognition.onerror = function () {

        voiceBtn.innerText = "🎤";

        addBotMessage(
            "Voice recognition failed."
        );
    };

    recognition.onend = function () {

        voiceBtn.innerText = "🎤";
    };
}

// =========================
// SAVE NOTE
// =========================

async function saveNote() {

    const noteText =
        document.getElementById(
            "note-text"
        );

    const note =
        noteText.value.trim();

    if (note === "") {

        alert("Enter a note first.");

        return;
    }

    try {

        const response =
            await fetch(
                "/save_note",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        note: note
                    })
                }
            );

        const data =
            await response.json();

        if (data.success) {

            noteText.value = "";

            loadNotes();
        }

    } catch (error) {

        console.error(error);
    }
}

// =========================
// LOAD NOTES
// =========================

async function loadNotes() {

    try {

        const response =
            await fetch("/get_notes");

        const notes =
            await response.json();

        const notesList =
            document.getElementById(
                "notes-list"
            );

        notesList.innerHTML = "";

        notes.forEach(
            (note, index) => {

                const noteDiv =
                    document.createElement(
                        "div"
                    );

                noteDiv.className =
                    "note-item";

                noteDiv.innerHTML = `
                    <span>${escapeHtml(note)}</span>

                    <button
                        onclick="deleteNote(${index})">
                        Delete
                    </button>
                `;

                notesList.appendChild(
                    noteDiv
                );
            }
        );

    } catch (error) {

        console.error(error);
    }
}

// =========================
// DELETE NOTE
// =========================

async function deleteNote(index) {

    try {

        await fetch(
            "/delete_note",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    index: index
                })
            }
        );

        loadNotes();

    } catch (error) {

        console.error(error);
    }
}

// =========================
// ESCAPE HTML
// =========================

function escapeHtml(text) {

    const div =
        document.createElement("div");

    div.innerText = text;

    return div.innerHTML;
}

// =========================
// INITIALIZE
// =========================

window.onload = function () {

    loadNotes();

    scrollToBottom();
};
function showSection(section){

    document.querySelectorAll(".section")
    .forEach(sec => sec.classList.add("hidden"));

    document.getElementById(section + "-section")
    .classList.remove("hidden");

    document.querySelectorAll(".menu-btn")
    .forEach(btn => btn.classList.remove("active"));

    event.target.closest(".menu-btn")
    .classList.add("active");
}
function startQuiz(subject){

    document.getElementById("user-input")
    .value = "quiz " + subject;

    sendMessage();

    document.getElementById(
        "quiz-result"
    ).innerHTML =

    "Quiz loaded: " +
    subject.toUpperCase();
}