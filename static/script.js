async function getPlan() {
    const subject = document.getElementById("subject").value;
    const hours = document.getElementById("hours").value;
    const weakness = document.getElementById("weakness").value;

    const response = await fetch("/plan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            subject: subject,
            hours: hours,
            weakness: weakness
        })
    });

    const data = await response.json();

    const result = document.getElementById("result");
    result.innerHTML = "";

    data.plan.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item;
        result.appendChild(li);
    });
}


async function sendMessage() {
    const message = document.getElementById("chatInput").value;

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

    document.getElementById("chatResponse").textContent = data.reply;
}