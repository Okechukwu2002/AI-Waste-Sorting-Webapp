

from flask import Flask, request, render_template_string, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import base64
import io
from datetime import datetime

app = Flask(__name__)

# Load model and labels
model = load_model("waste-classification-model.h5")
labels = ["Compost", "Trash", "Metal", "Plastic", "Glass", "Paper"]

# Store classification history (in-memory list)
classification_history = []

# Pages
HOME_PAGE = """
<h2>Welcome to JET FABLAB Waste AI Sorting Tool</h2>
<p>This AI-powered system classifies waste into categories like Compost, Trash, Metal, etc., and helps sort them in real-time using your camera.</p>
"""

ABOUT_PAGE = """
<h2>About This App</h2>
<p>The JET Waste AI Sorting Tool is an intelligent web application that uses a trained deep learning model to detect and classify waste using your camera. It helps reduce waste pollution and supports eco-friendly practices through accurate real-time categorization.</p>
"""

INSTRUCTIONS_PAGE = """
<h2>Instructions</h2>
<ol>
  <li>Ensure your webcam is working.</li>
  <li>Allow camera access when prompted.</li>
  <li>Point the camera at a waste item.</li>
  <li>The app will display the category and sorting direction.</li>
</ol>
"""

CONTACT_PAGE = """
<h2>Contact</h2>
<p>Email: jetsamjoseph@gmail.com</p>
<p>Phone: +2349031495094</p>
"""

# Main UI Template with camera and history
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>JET Waste AI Sorting Tool</title>
  <style>
    body { font-family: Arial; background: #1b2735; color: white; text-align: center; margin: 0; padding: 0; }
    header, nav { background-color: #0d47a1; padding: 20px; }
    nav a { color: white; text-decoration: none; margin: 0 15px; }
    nav a:hover { text-decoration: underline; }
    #content { padding: 30px; }
    video { border: 4px solid white; border-radius: 10px; }
    #result { margin-top: 15px; font-size: 1.5em; }
    .history { margin-top: 30px; text-align: center; }
    .history-item { display: inline-block; background: #263238; margin: 10px; padding: 10px; border-radius: 8px; }
    .history-item img { width: 100px; height: 100px; border-radius: 6px; border: 2px solid white; }
    .history-item p { margin: 5px 0; font-size: 0.9em; }
  </style>
</head>
<body>
  <header><h1>JET Waste AI Sorting Tool</h1></header>
  <nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/instructions">Instructions</a>
    <a href="/contact">Contact</a>
  </nav>
  <div id="content">{{ content|safe }}</div>
  {% if show_camera %}
    <video id="video" width="480" height="360" autoplay muted></video>
    <canvas id="canvas" style="display:none;"></canvas>
    <div id="result">Loading...</div>

    <div class="history">
      <h3>Classification History</h3>
      <div id="history-items"></div>
    </div>

    <script>
      const video = document.getElementById('video');
      const canvas = document.getElementById('canvas');
      const result = document.getElementById('result');
      const ctx = canvas.getContext('2d');
      const historyContainer = document.getElementById('history-items');

      navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => video.srcObject = stream)
        .catch(err => console.error('Camera access error:', err));

      function classifyImage() {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        ctx.drawImage(video, 0, 0);
        const imgData = canvas.toDataURL('image/jpeg');

        fetch('/classify', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ image: imgData })
        })
        .then(res => res.json())
        .then(data => {
          if (data.category) {
            result.textContent = 'Detected: ' + data.category;
            updateHistory(data.history);
          } else {
            result.textContent = 'Error: ' + data.error;
          }
        })
        .catch(err => result.textContent = 'Error: ' + err);
      }

      function updateHistory(items) {
        historyContainer.innerHTML = '';
        items.forEach(item => {
          const div = document.createElement('div');
          div.className = 'history-item';
          div.innerHTML = `
            <img src="${item.image}" />
            <p><strong>${item.label}</strong></p>
            <p>${item.time}</p>
          `;
          historyContainer.appendChild(div);
        });
      }

      setInterval(classifyImage, 2000);
    </script>
  {% endif %}
</body>
</html>
"""

# Image preprocessing
def preprocess_image(img_data):
    img = Image.open(io.BytesIO(img_data)).convert("RGB")
    img = img.resize((32, 32))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Routes
@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, content=HOME_PAGE, show_camera=True)

@app.route('/about')
def about():
    return render_template_string(HTML_TEMPLATE, content=ABOUT_PAGE, show_camera=False)

@app.route('/instructions')
def instructions():
    return render_template_string(HTML_TEMPLATE, content=INSTRUCTIONS_PAGE, show_camera=False)

@app.route('/contact')
def contact():
    return render_template_string(HTML_TEMPLATE, content=CONTACT_PAGE, show_camera=False)

@app.route('/classify', methods=['POST'])
def classify():
    try:
        img_data = request.json['image'].split(',')[1]
        img_bytes = base64.b64decode(img_data)
        img_array = preprocess_image(img_bytes)
        prediction = model.predict(img_array)
        index = int(np.argmax(prediction))
        label = labels[index] if index < len(labels) else "Unknown"

        # Keep last 5 images in history
        classification_history.insert(0, {
            'image': request.json['image'],
            'label': label,
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        if len(classification_history) > 5:
            classification_history.pop()

        return jsonify({'category': label, 'history': classification_history})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
