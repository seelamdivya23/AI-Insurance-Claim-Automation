function showForm(type) {
    document.getElementById("task").value = type;

    if (type === "claim") {
        document.getElementById("claim-form").style.display = "block";
        document.getElementById("fraud-form").style.display = "none";
    } else {
        document.getElementById("claim-form").style.display = "none";
        document.getElementById("fraud-form").style.display = "block";
    }
}
// ✨ Typing Effect
const text = "AI Insurance Claim Automation System";
let i = 0;

function typingEffect() {
    if (i < text.length) {
        document.querySelector(".typing").innerHTML += text.charAt(i);
        i++;
        setTimeout(typingEffect, 60);
    }
}

typingEffect();


// 🌙 Dark Mode Toggle
function toggleMode() {
    document.body.classList.toggle("dark-mode");
}
function showForm(type) {
    document.getElementById("task").value = type;

    if (type === "claim") {
        document.getElementById("claim-form").style.display = "block";
        document.getElementById("fraud-form").style.display = "none";
    } else {
        document.getElementById("claim-form").style.display = "none";
        document.getElementById("fraud-form").style.display = "block";
    }
}
