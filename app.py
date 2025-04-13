

from flask import Flask, request, render_template_string, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import io
from PIL import Image
import base64

app = Flask(__name__)

# Load the trained model
model = load_model("waste-classification-model.h5")
labels = ["Compost", "Trash", "Metal"]

def preprocess_image(img_data):
    img = Image.open(io.BytesIO(img_data)).convert("RGB")
    img = img.resize((32, 32))  # Match model input
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

# Embedded frontend template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>JET Waste AI Sorting Tool</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            color: white;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        header {
            padding: 30px;
            font-size: 2.5em;
            background-color: #0d47a1;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            text-align: left;
            padding-left: 50px;
        }
        nav {
            background-color: #0d47a1;
            padding: 10px;
            margin-bottom: 20px;
        }
        nav a {
            color: white;
            text-decoration: none;
            padding: 10px;
            font-size: 1.1em;
        }
        nav a:hover {
            background-color: #203a43;
        }
        #arrow {
            font-size: 60px;
            margin-top: 20px;
            opacity: 0;
            transition: all 0.5s ease;
        }
        #arrow.show {
            opacity: 1;
            animation: moveArrow 1.2s ease-in-out infinite;
        }
        #result {
            font-size: 1.5em;
            margin-top: 10px;
        }
        #video {
            border: 6px solid #ffffff33;
            border-radius: 15px;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.5);
            margin-top: 20px;
        }
        .history {
            margin-top: 20px;
            padding: 10px;
            background-color: #1c2b38;
            border-radius: 10px;
        }
        .history-item {
            display: flex;
            align-items: center;
            margin: 10px 0;
        }
        .history-item img {
            width: 50px;
            height: 50px;
            margin-right: 10px;
        }
        .history-item .label {
            font-size: 1.2em;
            margin-right: 15px;
        }
        .history-item .time {
            font-size: 0.9em;
            color: #ccc;
        }
        @keyframes moveArrow {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-12px); }
        }
    </style>
</head>
<body>
    <header>JET Waste AI Sorting Tool</header>
    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Instructions</a>
        <a href="#">Contact</a>
    </nav>
    <div>
        <video id="video" width="480" height="360" autoplay muted></video>
        <div id="result">Loading...</div>
        <div id="arrow">🔄</div>
    </div>

    <div class="history">
        <h3>Classification History</h3>
        <div id="history-list"></div>
    </div>

    <audio id="compost-sound" src="https://www.soundjay.com/buttons/sounds/button-30.mp3"></audio>
    <audio id="trash-sound" src="https://www.soundjay.com/buttons/sounds/button-10.mp3"></audio>
    <audio id="metal-sound" src="https://www.soundjay.com/buttons/sounds/button-16.mp3"></audio>

    <canvas id="canvas" style="display:none;"></canvas>

    <script>
        const video = document.getElementById('video');
        const canvas = document.getElementById('canvas');
        const result = document.getElementById('result');
        const arrow = document.getElementById('arrow');
        const historyList = document.getElementById('history-list');

        const compostSound = document.getElementById('compost-sound');
        const trashSound = document.getElementById('trash-sound');
        const metalSound = document.getElementById('metal-sound');

        const context = canvas.getContext('2d');

        let classificationHistory = [];

        navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => video.srcObject = stream)
            .catch(error => console.error('Camera error:', error));

        function classifyImage() {
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            context.drawImage(video, 0, 0);
            const imageData = canvas.toDataURL('image/jpeg');

            fetch('/classify', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ image: imageData })
            })
            .then(response => response.json())
            .then(data => {
                result.innerText = 'Detected: ' + data.category;
                arrow.classList.add('show');

                switch (data.category) {
                    case 'Compost':
                        arrow.innerText = '⬅️ Compost Bin';
                        compostSound.play();
                        break;
                    case 'Trash':
                        arrow.innerText = '⬇️ Trash Bin';
                        trashSound.play();
                        break;
                    case 'Metal':
                        arrow.innerText = '➡️ Metal Bin';
                        metalSound.play();
                        break;
                    default:
                        arrow.innerText = '❓ Unknown';
                        arrow.classList.remove('show');
                }

                classificationHistory.unshift({
                    category: data.category,
                    imageData: imageData,
                    time: new Date().toLocaleString()
                });

                if (classificationHistory.length > 5) {
                    classificationHistory.pop();
                }

                updateHistory();
            })
            .catch(err => {
                result.innerText = 'Error: ' + err;
                arrow.innerText = '';
            });
        }

        function updateHistory() {
            historyList.innerHTML = '';
            classificationHistory.forEach(item => {
                const historyItem = document.createElement('div');
                historyItem.classList.add('history-item');
                historyItem.innerHTML = `
                    <img src="${item.imageData}" alt="Waste" />
                    <div class="label">${item.category}</div>
                    <div class="time">${item.time}</div>
                `;
                historyList.appendChild(historyItem);
            });
        }

        setInterval(classifyImage, 1000);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/classify', methods=['POST'])
def classify():
    try:
        img_data = request.json['image'].split(',')[1]
        img_bytes = base64.b64decode(img_data)
        img_array = preprocess_image(img_bytes)
        prediction = model.predict(img_array)
        category = labels[np.argmax(prediction)]
        return jsonify({'category': category})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


