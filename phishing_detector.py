<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Phishing Detector PRO</title>

    <style>
        body {
            margin: 0;
            padding: 0;
            background: radial-gradient(circle, #000000, #001a0f);
            height: 100vh;
            font-family: "Poppins", sans-serif;
            color: #00ffb3;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Matrix Rain Background */
        canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.22;
        }

        .card {
            width: 500px;
            padding: 30px;
            border-radius: 18px;
            background: rgba(0, 0, 0, 0.85);
            border: 1px solid #00ffb3;
            box-shadow: 0 0 25px #00ffb3;
            text-align: center;
            animation: pop 0.5s ease-out;
            z-index: 10;
        }

        @keyframes pop {
            from { transform: scale(0.6); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }

        input {
            width: 100%;
            padding: 12px;
            margin-top: 15px;
            font-size: 16px;
            border-radius: 8px;
            background: #111;
            color: #00ffb3;
            border: 1px solid #00ffb3;
        }

        button {
            width: 100%;
            padding: 12px;
            margin-top: 15px;
            background: #00ffb3;
            font-size: 17px;
            border-radius: 8px;
            border: none;
            color: black;
            font-weight: bold;
            cursor: pointer;
        }

        button:hover {
            box-shadow: 0 0 20px #00ffb3;
        }

        #resultBox {
            margin-top: 20px;
            padding: 15px;
            border-radius: 12px;
            font-size: 18px;
            font-weight: bold;
        }

        .danger {
            border: 1px solid #ff4d4d;
            color: #ff4d4d;
            box-shadow: 0 0 15px #ff4d4d;
        }

        .safe {
            border: 1px solid #00ffaa;
            color: #00ffaa;
            box-shadow: 0 0 15px #00ffaa;
        }

        .reasons {
            margin-top: 15px;
            text-align: left;
            font-size: 14px;
            color: #e6e6e6;
        }

        .reasons li {
            margin-bottom: 6px;
        }
    </style>
</head>
<body>

<!-- Matrix Rain Canvas -->
<canvas id="matrixCanvas"></canvas>

<div class="card">
    <h2>🛡️ Phishing Detector PRO</h2>
    <p>Advanced Scanner with Accuracy & Suspicion Analysis</p>

    <input id="url" placeholder="Enter URL to scan...">
    <button onclick="scan()">Scan Now</button>

    <div id="resultBox"></div>
    <ul id="reasons" class="reasons"></ul>
</div>

<script>
/* MATRIX RAIN SCRIPT */
const canvas = document.getElementById("matrixCanvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const letters = "011 101 001 110 0101 010 111 0010 110 0101 10 101 0101";
const lettersArr = letters.split("");

const fontSize = 18;
const columns = canvas.width / fontSize;

const drops = [];
for (let i = 0; i < columns; i++) {
    drops[i] = 1;
}

function drawMatrix() {
    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#00ffb3";
    ctx.font = fontSize + "px monospace";

    for (let i = 0; i < drops.length; i++) {
        const text = lettersArr[Math.floor(Math.random() * lettersArr.length)];
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);

        if (drops[i] * fontSize > canvas.height && Math.random() > 0.95) {
            drops[i] = 0;
        }
        drops[i]++;
    }
}

setInterval(drawMatrix, 40);

/* PHISHING DETECTOR SCRIPT */
function scan() {
    let url = document.getElementById("url").value;
    let resultBox = document.getElementById("resultBox");
    let reasonList = document.getElementById("reasons");
    reasonList.innerHTML = "";

    if (url.trim() === "") {
        resultBox.className = "danger";
        resultBox.innerHTML = "❗ Enter a URL first";
        return;
    }

    let score = 0;
    let reasons = [];

    if (url.includes("@")) { score++; reasons.push("Contains '@' symbol (Used to redirect users)"); }
    if (url.length > 75) { score++; reasons.push("URL is very long (Common in phishing attempts)"); }
    if (/http[s]?:\/\/\d+\.\d+\.\d+\.\d+/.test(url)) { score++; reasons.push("Uses IP instead of domain"); }
    if (url.split(".").length > 4) { score++; reasons.push("Contains too many dots"); }
    if (url.includes("-")) { score++; reasons.push("Suspicious hyphens in URL"); }

    let dangerPercent = (score / 5) * 100;

    if (score >= 3) {
        resultBox.className = "danger";
        resultBox.innerHTML = `⚠️ Phishing Detected <br>🔥 Danger Level: ${dangerPercent.toFixed(0)}%`;
    } else {
        resultBox.className = "safe";
        resultBox.innerHTML = `✅ Safe URL <br>🛡️ Risk Level: ${dangerPercent.toFixed(0)}%`;
    }

    reasons.forEach(r => {
        let li = document.createElement("li");
        li.textContent = "• " + r;
        reasonList.appendChild(li);
    });
}
</script>

</body>
</html>
