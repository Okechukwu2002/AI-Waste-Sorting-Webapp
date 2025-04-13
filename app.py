# # from flask import Flask, render_template_string, Response, jsonify
# # import cv2
# # import numpy as np
# # import tensorflow as tf
# # from tensorflow.keras.models import load_model
# #
# # app = Flask(__name__)
# #
# # def initialize_model():
# #     model = load_model("waste_classifier.h5")
# #     labels = ["compost", "trash", "metal"]
# #     return model, labels
# #
# # model, labels = initialize_model()
# # cap = cv2.VideoCapture(0)
# #
# # def classify_waste(image, model, labels):
# #     image = cv2.resize(image, (224, 224))
# #     image = np.expand_dims(image, axis=0) / 255.0
# #     prediction = model.predict(image)
# #     class_index = np.argmax(prediction)
# #     return labels[class_index]
# #
# # def generate_frames():
# #     while True:
# #         success, frame = cap.read()
# #         if not success:
# #             break
# #         else:
# #             ret, buffer = cv2.imencode('.jpg', frame)
# #             frame = buffer.tobytes()
# #             yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
# #
# # html_page = '''
# # <!DOCTYPE html>
# # <html lang="en">
# # <head>
# #     <meta charset="UTF-8">
# #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
# #     <title>Smart Waste Sorting System</title>
# #     <link rel="icon" href="data:,">
# #     <style>
# #         body {
# #             font-family: 'Segoe UI', sans-serif;
# #             background: linear-gradient(to right, #141e30, #243b55);
# #             color: white;
# #             text-align: center;
# #             padding: 20px;
# #         }
# #         h1 {
# #             margin-bottom: 20px;
# #             font-size: 2.5rem;
# #         }
# #         .video-container {
# #             border: 4px solid #fff;
# #             border-radius: 20px;
# #             overflow: hidden;
# #             display: inline-block;
# #             margin-bottom: 20px;
# #             box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.5);
# #         }
# #         .result {
# #             font-size: 1.8rem;
# #             margin-top: 20px;
# #             font-weight: bold;
# #         }
# #         button {
# #             padding: 12px 30px;
# #             font-size: 18px;
# #             background-color: #2980b9;
# #             color: white;
# #             border: none;
# #             border-radius: 8px;
# #             cursor: pointer;
# #             margin-top: 15px;
# #             transition: background-color 0.3s;
# #         }
# #         button:hover {
# #             background-color: #3498db;
# #         }
# #         .arrow {
# #             font-size: 3em;
# #             margin-top: 15px;
# #         }
# #         footer {
# #             margin-top: 30px;
# #             font-size: 0.9em;
# #             color: #ccc;
# #         }
# #     </style>
# # </head>
# # <body>
# #     <h1>Intelligent Waste Sorting System</h1>
# #     <div class="video-container">
# #         <img id="video" src="{{ url_for('video_feed') }}" width="640" height="480">
# #     </div>
# #     <div>
# #         <button onclick="classifyWaste()">Classify Waste</button>
# #     </div>
# #     <div class="result" id="result"></div>
# #     <div class="arrow" id="arrow"></div>
# #     <footer>Developed by JET Technologies</footer>
# #
# #     <script>
# #         function speak(text) {
# #             const synth = window.speechSynthesis;
# #             const utterThis = new SpeechSynthesisUtterance(text);
# #             utterThis.lang = 'en-US';
# #             synth.speak(utterThis);
# #         }
# #
# #         function classifyWaste() {
# #             fetch('{{ url_for('classify') }}')
# #                 .then(response => response.json())
# #                 .then(data => {
# #                     let result = document.getElementById("result");
# #                     let arrow = document.getElementById("arrow");
# #
# #                     if (data.waste_type === "compost") {
# #                         result.innerText = "Classified as: Compost/Food Waste";
# #                         arrow.innerText = "⬅️ Use the Compost Bin";
# #                         speak("Please place the item in the compost bin on the left.");
# #                     } else if (data.waste_type === "trash") {
# #                         result.innerText = "Classified as: Trash";
# #                         arrow.innerText = "⬆️ Use the Trash Bin";
# #                         speak("Please place the item in the trash bin in the middle.");
# #                     } else if (data.waste_type === "metal") {
# #                         result.innerText = "Classified as: Metallic Waste";
# #                         arrow.innerText = "➡️ Use the Metal Bin";
# #                         speak("Please place the item in the metal bin on the right.");
# #                     } else {
# #                         result.innerText = "Classification Failed";
# #                         arrow.innerText = "";
# #                         speak("Sorry, the item could not be classified.");
# #                     }
# #                 });
# #         }
# #     </script>
# # </body>
# # </html>
# # '''
# #
# # @app.route('/')
# # def index():
# #     return render_template_string(html_page)
# #
# # @app.route('/video_feed')
# # def video_feed():
# #     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
# #
# # @app.route('/classify')
# # def classify():
# #     success, frame = cap.read()
# #     if success:
# #         waste_type = classify_waste(frame, model, labels)
# #         return jsonify({"waste_type": waste_type})
# #     return jsonify({"error": "No frame captured"})
# #
# # @app.teardown_appcontext
# # def cleanup(exception):
# #     cap.release()
# #     cv2.destroyAllWindows()
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
#
#
#
#
# from flask import Flask, render_template_string, Response, jsonify
# import cv2
# import numpy as np
# try:
#     import tensorflow as tf
#     from tensorflow.keras.models import load_model
# except ImportError as e:
#     raise ImportError("Failed to import TensorFlow. Please ensure TensorFlow is installed correctly.") from e
#
# app = Flask(__name__)
#
# def initialize_model():
#     try:
#         model = load_model("waste_classifier.h5")
#         labels = ["compost", "trash", "metal"]
#         return model, labels
#     except Exception as e:
#         raise RuntimeError("Failed to load the model. Please ensure the model file is correct.") from e
#
# model, labels = initialize_model()
# cap = cv2.VideoCapture(0)
#
# def classify_waste(image, model, labels):
#     try:
#         image = cv2.resize(image, (224, 224))
#         image = np.expand_dims(image, axis=0) / 255.0
#         prediction = model.predict(image)
#         class_index = np.argmax(prediction)
#         return labels[class_index]
#     except Exception as e:
#         raise RuntimeError("Failed to classify the waste. Please check the model and input image.") from e
#
# def generate_frames():
#     while True:
#         success, frame = cap.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#
# html_page = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Smart Waste Sorting System</title>
#     <link rel="icon" href="data:,">
#     <style>
#         body {
#             font-family: 'Segoe UI', sans-serif;
#             background: linear-gradient(to right, #141e30, #243b55);
#             color: white;
#             text-align: center;
#             padding: 20px;
#         }
#         h1 {
#             margin-bottom: 20px;
#             font-size: 2.5rem;
#         }
#         .video-container {
#             border: 4px solid #fff;
#             border-radius: 20px;
#             overflow: hidden;
#             display: inline-block;
#             margin-bottom: 20px;
#             box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.5);
#         }
#         .result {
#             font-size: 1.8rem;
#             margin-top: 20px;
#             font-weight: bold;
#         }
#         button {
#             padding: 12px 30px;
#             font-size: 18px;
#             background-color: #2980b9;
#             color: white;
#             border: none;
#             border-radius: 8px;
#             cursor: pointer;
#             margin-top: 15px;
#             transition: background-color 0.3s;
#         }
#         button:hover {
#             background-color: #3498db;
#         }
#         .arrow {
#             font-size: 3em;
#             margin-top: 15px;
#         }
#         footer {
#             margin-top: 30px;
#             font-size: 0.9em;
#             color: #ccc;
#         }
#     </style>
# </head>
# <body>
#     <h1>Intelligent Waste Sorting System</h1>
#     <div class="video-container">
#         <img id="video" src="{{ url_for('video_feed') }}" width="640" height="480">
#     </div>
#     <div>
#         <button onclick="classifyWaste()">Classify Waste</button>
#     </div>
#     <div class="result" id="result"></div>
#     <div class="arrow" id="arrow"></div>
#     <footer>Developed by JET Technologies</footer>
#
#     <script>
#         function speak(text) {
#             const synth = window.speechSynthesis;
#             const utterThis = new SpeechSynthesisUtterance(text);
#             utterThis.lang = 'en-US';
#             synth.speak(utterThis);
#         }
#
#         function classifyWaste() {
#             fetch('{{ url_for('classify') }}')
#                 .then(response => response.json())
#                 .then(data => {
#                     let result = document.getElementById("result");
#                     let arrow = document.getElementById("arrow");
#
#                     if (data.waste_type === "compost") {
#                         result.innerText = "Classified as: Compost/Food Waste";
#                         arrow.innerText = "⬅️ Use the Compost Bin";
#                         speak("Please place the item in the compost bin on the left.");
#                     } else if (data.waste_type === "trash") {
#                         result.innerText = "Classified as: Trash";
#                         arrow.innerText = "⬆️ Use the Trash Bin";
#                         speak("Please place the item in the trash bin in the middle.");
#                     } else if (data.waste_type === "metal") {
#                         result.innerText = "Classified as: Metallic Waste";
#                         arrow.innerText = "➡️ Use the Metal Bin";
#                         speak("Please place the item in the metal bin on the right.");
#                     } else {
#                         result.innerText = "Classification Failed";
#                         arrow.innerText = "";
#                         speak("Sorry, the item could not be classified.");
#                     }
#                 });
#         }
#     </script>
# </body>
# </html>
# '''
#
# @app.route('/')
# def index():
#     return render_template_string(html_page)
#
# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
#
# @app.route('/classify')
# def classify():
#     success, frame = cap.read()
#     if success:
#         waste_type = classify_waste(frame, model, labels)
#         return jsonify({"waste_type": waste_type})
#     return jsonify({"error": "No frame captured"})
#
# @app.teardown_appcontext
# def cleanup(exception):
#     cap.release()
#     cv2.destroyAllWindows()
#
# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template_string, request, jsonify
# import numpy as np
# import cv2
# import os
# from tensorflow.keras.models import load_model
#
# app = Flask(__name__)
#
# # Load the pre-trained model
# model_path = os.path.join(os.getcwd(), 'waste_classifier.h5')
# model = load_model(model_path)
# labels = ["Compost", "Trash", "Metal"]  # Update based on your model's classes
#
# def preprocess_image(image):
#     """Preprocess the image to match model input requirements."""
#     resized_image = cv2.resize(image, (224, 224))  # Adjust size as per your model
#     normalized_image = resized_image / 255.0
#     return np.expand_dims(normalized_image, axis=0)
#
# @app.route('/')
# def index():
#     # HTML template with embedded CSS and JavaScript
#     return render_template_string('''
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <title>Waste Classifier</title>
#         <link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}">
#
#         <style>
#             body {
#                 font-family: Arial, sans-serif;
#                 background-color: #f4f4f4;
#                 text-align: center;
#                 padding-top: 50px;
#             }
#             .container {
#                 background-color: #fff;
#                 padding: 20px;
#                 border-radius: 5px;
#                 box-shadow: 0 0 10px rgba(0,0,0,0.1);
#                 display: inline-block;
#             }
#             input[type="file"] {
#                 margin: 10px 0;
#             }
#             button {
#                 padding: 10px 20px;
#                 background-color: #5cb85c;
#                 color: #fff;
#                 border: none;
#                 border-radius: 5px;
#                 cursor: pointer;
#             }
#             #result {
#                 margin-top: 20px;
#                 font-size: 1.2em;
#             }
#         </style>
#     </head>
#     <body>
#         <div class="container">
#             <h1>Waste Classification</h1>
#             <form id="upload-form" enctype="multipart/form-data">
#                 <input type="file" name="file" id="file" accept="image/*" required>
#                 <button type="submit">Classify</button>
#             </form>
#             <div id="result"></div>
#         </div>
#         <script>
#             document.getElementById('upload-form').onsubmit = async function(e) {
#                 e.preventDefault();
#                 const fileInput = document.getElementById('file');
#                 if (fileInput.files.length === 0) {
#                     alert('Please select an image.');
#                     return;
#                 }
#                 const formData = new FormData();
#                 formData.append('file', fileInput.files[0]);
#
#                 const response = await fetch('/classify', {
#                     method: 'POST',
#                     body: formData
#                 });
#
#                 const result = await response.json();
#                 if (response.ok) {
#                     document.getElementById('result').textContent = 'Predicted Category: ' + result.category;
#                 } else {
#                     document.getElementById('result').textContent = 'Error: ' + result.error;
#                 }
#             };
#         </script>
#     </body>
#     </html>
#     ''')
#
# @app.route('/classify', methods=['POST'])
# def classify():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file uploaded'}), 400
#
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No file selected'}), 400
#
#     # Read the image file
#     file_bytes = np.frombuffer(file.read(), np.uint8)
#     image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#
#     # Preprocess the image
#     processed_image = preprocess_image(image)
#
#     # Perform prediction
#     predictions = model.predict(processed_image)
#     class_index = np.argmax(predictions)
#     category = labels[class_index]
#
#     return jsonify({'category': category})
#
# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, render_template_string, request, jsonify
# import numpy as np
# import cv2
# import os
# import base64
# from tensorflow.keras.models import load_model
#
# app = Flask(__name__)
#
# # Load the pre-trained model
# model_path = os.path.join(os.getcwd(), 'waste_classifier.h5')
# model = load_model(model_path)
# labels = ["Compost", "Trash", "Metal"]  # Your model's classes
#
# def preprocess_image(image):
#     resized_image = cv2.resize(image, (224, 224))
#     normalized_image = resized_image / 255.0
#     return np.expand_dims(normalized_image, axis=0)
#
# @app.route('/')
# def index():
#     return render_template_string('''
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>Smart Waste Sorter</title>
#     <style>
#         body {
#             font-family: 'Segoe UI', sans-serif;
#             background: linear-gradient(to right, #2c3e50, #3498db);
#             color: white;
#             text-align: center;
#             padding: 30px;
#         }
#         h1 {
#             margin-bottom: 10px;
#         }
#         #camera {
#             border-radius: 10px;
#             box-shadow: 0 0 20px rgba(0,0,0,0.3);
#             margin-top: 20px;
#         }
#         #arrow {
#             font-size: 60px;
#             margin: 30px 0;
#         }
#         button {
#             background-color: #1abc9c;
#             color: white;
#             border: none;
#             padding: 12px 24px;
#             font-size: 16px;
#             border-radius: 5px;
#             cursor: pointer;
#             margin-top: 20px;
#         }
#         button:hover {
#             background-color: #16a085;
#         }
#     </style>
# </head>
# <body>
#     <h1>Smart Waste Sorting System</h1>
#     <video id="camera" width="500" height="375" autoplay></video>
#     <div>
#         <button onclick="captureAndClassify()">Classify Waste</button>
#     </div>
#     <div id="result"></div>
#     <div id="arrow"></div>
#
#     <script>
#         const video = document.getElementById('camera');
#         const result = document.getElementById('result');
#         const arrow = document.getElementById('arrow');
#
#         navigator.mediaDevices.getUserMedia({ video: true })
#             .then(stream => video.srcObject = stream)
#             .catch(error => console.error('Camera error:', error));
#
#         function captureAndClassify() {
#             const canvas = document.createElement('canvas');
#             canvas.width = video.videoWidth;
#             canvas.height = video.videoHeight;
#             canvas.getContext('2d').drawImage(video, 0, 0);
#             const imageData = canvas.toDataURL('image/jpeg');
#
#             fetch('/classify', {
#                 method: 'POST',
#                 headers: { 'Content-Type': 'application/json' },
#                 body: JSON.stringify({ image: imageData })
#             })
#             .then(response => response.json())
#             .then(data => {
#                 result.innerText = 'Detected: ' + data.category;
#                 if (data.category === 'Compost') {
#                     arrow.innerText = '⬅️ Put in Compost Bin';
#                 } else if (data.category === 'Trash') {
#                     arrow.innerText = '⬇️ Put in Trash Bin';
#                 } else if (data.category === 'Metal') {
#                     arrow.innerText = '➡️ Put in Metal Bin';
#                 }
#             })
#             .catch(err => {
#                 result.innerText = 'Error: ' + err;
#                 arrow.innerText = '';
#             });
#         }
#     </script>
# </body>
# </html>
# ''')
#
# @app.route('/classify', methods=['POST'])
# def classify():
#     data = request.get_json()
#     if not data or 'image' not in data:
#         return jsonify({'error': 'No image received'}), 400
#
#     image_data = data['image'].split(',')[1]
#     file_bytes = np.frombuffer(base64.b64decode(image_data), np.uint8)
#     image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#
#     if image is None:
#         return jsonify({'error': 'Failed to decode image'}), 400
#
#     processed_image = preprocess_image(image)
#     prediction = model.predict(processed_image)
#     class_index = np.argmax(prediction)
#     category = labels[class_index]
#
#     return jsonify({'category': category})
#
# if __name__ == '__main__':
#     app.run(debug=True)






# from flask import Flask, render_template_string, request, jsonify
# import numpy as np
# import cv2
# import os
# import base64
# from tensorflow.keras.models import load_model
#
# app = Flask(__name__)
#
# # Load model
# model_path = os.path.join(os.getcwd(), 'waste_classifier.h5')
# model = load_model(model_path)
# labels = ['Compost', 'Trash', 'Metal']
#
# # Image preprocessing
# def preprocess_image(image):
#     resized = cv2.resize(image, (224, 224))
#     normalized = resized / 255.0
#     return np.expand_dims(normalized, axis=0)
#
# # Home route
# @app.route('/')
# def index():
#     return render_template_string('''
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>Smart Waste Sorter</title>
#     <style>
#         body {
#             font-family: 'Segoe UI', sans-serif;
#             background: linear-gradient(120deg, #2c3e50, #3498db);
#             color: white;
#             text-align: center;
#             padding: 40px;
#         }
#         h1 {
#             font-size: 2.8em;
#             margin-bottom: 20px;
#         }
#         #camera {
#             border-radius: 15px;
#             box-shadow: 0 0 25px rgba(0,0,0,0.4);
#             margin-top: 20px;
#         }
#         #arrow {
#             font-size: 80px;
#             margin: 30px 0;
#             animation: float 1.5s ease-in-out infinite;
#         }
#         @keyframes float {
#             0%, 100% { transform: translateY(0); }
#             50% { transform: translateY(-10px); }
#         }
#         #result {
#             font-size: 24px;
#             margin-top: 20px;
#         }
#         button {
#             background-color: #1abc9c;
#             color: white;
#             border: none;
#             padding: 14px 28px;
#             font-size: 18px;
#             border-radius: 8px;
#             cursor: pointer;
#             margin-top: 25px;
#             transition: background 0.3s ease;
#         }
#         button:hover {
#             background-color: #16a085;
#         }
#     </style>
# </head>
# <body>
#     <h1>Smart Waste Sorting System</h1>
#     <video id="camera" width="480" height="360" autoplay muted></video>
#     <div id="result">Waiting for prediction...</div>
#     <div id="arrow">🔄</div>
#
#     <script>
#         const video = document.getElementById('camera');
#         const result = document.getElementById('result');
#         const arrow = document.getElementById('arrow');
#
#         navigator.mediaDevices.getUserMedia({ video: true })
#             .then(stream => video.srcObject = stream)
#             .catch(error => console.error('Camera error:', error));
#
#         function classifyFrame() {
#             const canvas = document.createElement('canvas');
#             canvas.width = video.videoWidth;
#             canvas.height = video.videoHeight;
#             canvas.getContext('2d').drawImage(video, 0, 0);
#             const imageData = canvas.toDataURL('image/jpeg');
#
#             fetch('/classify', {
#                 method: 'POST',
#                 headers: { 'Content-Type': 'application/json' },
#                 body: JSON.stringify({ image: imageData })
#             })
#             .then(response => response.json())
#             .then(data => {
#                 result.innerText = 'Detected: ' + data.category;
#                 switch (data.category) {
#                     case 'Compost':
#                         arrow.innerText = '⬅️ Put in Compost Bin';
#                         break;
#                     case 'Trash':
#                         arrow.innerText = '⬇️ Put in Trash Bin';
#                         break;
#                     case 'Metal':
#                         arrow.innerText = '➡️ Put in Metal Bin';
#                         break;
#                     default:
#                         arrow.innerText = '❓ Unknown';
#                 }
#             })
#             .catch(err => {
#                 result.innerText = 'Error: ' + err;
#                 arrow.innerText = '';
#             });
#         }
#
#         setInterval(classifyFrame, 3000);  // Classify every 3 seconds
#     </script>
# </body>
# </html>
# ''')
#
# # Classification route
# @app.route('/classify', methods=['POST'])
# def classify():
#     data = request.get_json()
#     if 'image' not in data:
#         return jsonify({'error': 'No image received'}), 400
#
#     image_data = data['image'].split(',')[1]
#     file_bytes = np.frombuffer(base64.b64decode(image_data), np.uint8)
#     image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#
#     if image is None:
#         return jsonify({'error': 'Failed to decode image'}), 400
#
#     processed_image = preprocess_image(image)
#     prediction = model.predict(processed_image)
#     class_index = np.argmax(prediction)
#     category = labels[class_index]
#
#     return jsonify({'category': category})
#
# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template_string, request, jsonify
# import numpy as np
# import cv2
# import os
# import base64
# from tensorflow.keras.models import load_model
#
# app = Flask(__name__)
#
# # Load pre-trained model
# model_path = os.path.join(os.getcwd(), 'waste-classification-model.h5')
# model = load_model(model_path)
# labels = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']  # Update these to match your model classes
#
#
# # Image preprocessing
# def preprocess_image(image):
#     resized = cv2.resize(image, (224, 224))  # Assuming model expects 224x224 input
#     normalized = resized / 255.0
#     return np.expand_dims(normalized, axis=0)
#
#
# # Home route
# @app.route('/')
# def index():
#     return render_template_string('''
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>Smart Waste Sorter</title>
#     <style>
#         body {
#             font-family: 'Segoe UI', sans-serif;
#             background: linear-gradient(120deg, #2c3e50, #3498db);
#             color: white;
#             text-align: center;
#             padding: 40px;
#         }
#         h1 {
#             font-size: 2.8em;
#             margin-bottom: 20px;
#         }
#         #camera {
#             border-radius: 15px;
#             box-shadow: 0 0 25px rgba(0,0,0,0.4);
#             margin-top: 20px;
#         }
#         #arrow {
#             font-size: 80px;
#             margin: 30px 0;
#             animation: float 1.5s ease-in-out infinite;
#         }
#         @keyframes float {
#             0%, 100% { transform: translateY(0); }
#             50% { transform: translateY(-10px); }
#         }
#         #result {
#             font-size: 24px;
#             margin-top: 20px;
#         }
#         button {
#             background-color: #1abc9c;
#             color: white;
#             border: none;
#             padding: 14px 28px;
#             font-size: 18px;
#             border-radius: 8px;
#             cursor: pointer;
#             margin-top: 25px;
#             transition: background 0.3s ease;
#         }
#         button:hover {
#             background-color: #16a085;
#         }
#     </style>
# </head>
# <body>
#     <h1>Smart Waste Sorting System</h1>
#     <video id="camera" width="480" height="360" autoplay muted></video>
#     <div id="result">Waiting for prediction...</div>
#     <div id="arrow">🔄</div>
#
#     <script>
#         const video = document.getElementById('camera');
#         const result = document.getElementById('result');
#         const arrow = document.getElementById('arrow');
#
#         navigator.mediaDevices.getUserMedia({ video: true })
#             .then(stream => video.srcObject = stream)
#             .catch(error => console.error('Camera error:', error));
#
#         function classifyFrame() {
#             const canvas = document.createElement('canvas');
#             canvas.width = video.videoWidth;
#             canvas.height = video.videoHeight;
#             canvas.getContext('2d').drawImage(video, 0, 0);
#             const imageData = canvas.toDataURL('image/jpeg');
#
#             fetch('/classify', {
#                 method: 'POST',
#                 headers: { 'Content-Type': 'application/json' },
#                 body: JSON.stringify({ image: imageData })
#             })
#             .then(response => {
#                 if (!response.ok) {
#                     throw new Error('Failed to classify image');
#                 }
#                 return response.json();
#             })
#             .then(data => {
#                 result.innerText = 'Detected: ' + data.category;
#                 switch (data.category.toLowerCase()) {
#                     case 'cardboard':
#                     case 'paper':
#                         arrow.innerText = '⬅️ Put in Compost Bin';
#                         break;
#                     case 'trash':
#                     case 'plastic':
#                         arrow.innerText = '⬇️ Put in Trash Bin';
#                         break;
#                     case 'metal':
#                     case 'glass':
#                         arrow.innerText = '➡️ Put in Metal Bin';
#                         break;
#                     default:
#                         arrow.innerText = '❓ Unknown';
#                 }
#             })
#             .catch(err => {
#                 result.innerText = 'Error: ' + err.message;
#                 arrow.innerText = '';
#             });
#         }
#
#         setInterval(classifyFrame, 3000);  // Classify every 3 seconds
#     </script>
# </body>
# </html>
# ''')
#
#
# # Classification route
# @app.route('/classify', methods=['POST'])
# def classify():
#     try:
#         data = request.get_json()
#         if 'image' not in data:
#             return jsonify({'error': 'No image received'}), 400
#
#         image_data = data['image'].split(',')[1]
#         file_bytes = np.frombuffer(base64.b64decode(image_data), np.uint8)
#         image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#
#         if image is None:
#             return jsonify({'error': 'Failed to decode image'}), 400
#
#         processed_image = preprocess_image(image)
#         prediction = model.predict(processed_image)
#         class_index = np.argmax(prediction)
#         category = labels[class_index]
#
#         return jsonify({'category': category})
#
#     except Exception as e:
#         return jsonify({'error': f'An error occurred: {str(e)}'}), 500
#
#
# if __name__ == '__main__':
#     app.run(debug=True)



#
# from flask import Flask, render_template_string, request, jsonify
# import numpy as np
# import cv2
# import os
# import base64
# from tensorflow.keras.models import load_model
#
# app = Flask(__name__)
#
# # Load pre-trained model
# model_path = os.path.join(os.getcwd(), 'waste-classification-model.h5')
# model = load_model(model_path)
# labels = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']  # Update these to match your model classes
#
# # Image preprocessing
# def preprocess_image(image):
#     resized = cv2.resize(image, (224, 224))  # Assuming model expects 224x224 input
#     normalized = resized / 255.0
#     return np.expand_dims(normalized, axis=0)
#
# # Home route
# @app.route('/')
# def index():
#     return render_template_string('''
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>Smart Waste Sorter</title>
#     <style>
#         body {
#             font-family: 'Segoe UI', sans-serif;
#             background: linear-gradient(120deg, #2c3e50, #3498db);
#             color: white;
#             text-align: center;
#             padding: 40px;
#         }
#         h1 {
#             font-size: 2.8em;
#             margin-bottom: 20px;
#         }
#         #camera {
#             border-radius: 15px;
#             box-shadow: 0 0 25px rgba(0,0,0,0.4);
#             margin-top: 20px;
#         }
#         #arrow {
#             font-size: 80px;
#             margin: 30px 0;
#             animation: float 1.5s ease-in-out infinite;
#         }
#         @keyframes float {
#             0%, 100% { transform: translateY(0); }
#             50% { transform: translateY(-10px); }
#         }
#         #result {
#             font-size: 24px;
#             margin-top: 20px;
#         }
#         button {
#             background-color: #1abc9c;
#             color: white;
#             border: none;
#             padding: 14px 28px;
#             font-size: 18px;
#             border-radius: 8px;
#             cursor: pointer;
#             margin-top: 25px;
#             transition: background 0.3s ease;
#         }
#         button:hover {
#             background-color: #16a085;
#         }
#     </style>
# </head>
# <body>
#     <h1>Smart Waste Sorting System</h1>
#     <video id="camera" width="480" height="360" autoplay muted></video>
#     <div id="result">Waiting for prediction...</div>
#     <div id="arrow">🔄</div>
#
#     <script>
#         const video = document.getElementById('camera');
#         const result = document.getElementById('result');
#         const arrow = document.getElementById('arrow');
#
#         navigator.mediaDevices.getUserMedia({ video: true })
#             .then(stream => video.srcObject = stream)
#             .catch(error => console.error('Camera error:', error));
#
#         function classifyFrame() {
#             const canvas = document.createElement('canvas');
#             canvas.width = video.videoWidth;
#             canvas.height = video.videoHeight;
#             canvas.getContext('2d').drawImage(video, 0, 0);
#             const imageData = canvas.toDataURL('image/jpeg');  // Send image as JPEG
#
#             console.log("Sending image data:", imageData);  // Debug log
#
#             fetch('/classify', {
#                 method: 'POST',
#                 headers: { 'Content-Type': 'application/json' },
#                 body: JSON.stringify({ image: imageData })
#             })
#             .then(response => {
#                 if (!response.ok) {
#                     throw new Error('Failed to classify image');
#                 }
#                 return response.json();
#             })
#             .then(data => {
#                 result.innerText = 'Detected: ' + data.category;
#                 switch (data.category.toLowerCase()) {
#                     case 'cardboard':
#                     case 'paper':
#                         arrow.innerText = '⬅️ Put in Compost Bin';
#                         break;
#                     case 'trash':
#                     case 'plastic':
#                         arrow.innerText = '⬇️ Put in Trash Bin';
#                         break;
#                     case 'metal':
#                     case 'glass':
#                         arrow.innerText = '➡️ Put in Metal Bin';
#                         break;
#                     default:
#                         arrow.innerText = '❓ Unknown';
#                 }
#             })
#             .catch(err => {
#                 result.innerText = 'Error: ' + err.message;
#                 arrow.innerText = '';
#             });
#         }
#
#         setInterval(classifyFrame, 3000);  // Classify every 3 seconds
#     </script>
# </body>
# </html>
# ''')
#
# # Classification route
# @app.route('/classify', methods=['POST'])
# def classify():
#     try:
#         data = request.get_json()
#         if 'image' not in data:
#             return jsonify({'error': 'No image received'}), 400
#
#         image_data = data['image'].split(',')[1]  # Remove base64 header part
#         file_bytes = np.frombuffer(base64.b64decode(image_data), np.uint8)
#         image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#
#         if image is None:
#             return jsonify({'error': 'Failed to decode image'}), 400
#
#         print("Image decoded successfully")  # Debug log
#
#         processed_image = preprocess_image(image)
#         prediction = model.predict(processed_image)
#         class_index = np.argmax(prediction)
#         category = labels[class_index]
#
#         return jsonify({'category': category})
#
#     except Exception as e:
#         return jsonify({'error': f'An error occurred: {str(e)}'}), 500
#
# if __name__ == '__main__':
#     app.run(debug=True)

#
# from flask import Flask, render_template_string, request, jsonify
# import numpy as np
# import cv2
# import os
# import base64
# from tensorflow.keras.models import load_model
#
# app = Flask(__name__)
#
# # Load pre-trained model
# model_path = os.path.join(os.getcwd(), 'waste-classification-model.h5')
# model = load_model(model_path)
# labels = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']  # Update these to match your model classes
#
#
# # Image preprocessing
# def preprocess_image(image):
#     resized = cv2.resize(image, (224, 224))  # Assuming model expects 224x224 input
#     normalized = resized / 255.0
#     return np.expand_dims(normalized, axis=0)
#
#
# # Home route
# @app.route('/')
# def index():
#     return render_template_string('''
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>Smart Waste Sorter</title>
#     <style>
#         body {
#             font-family: 'Segoe UI', sans-serif;
#             background: linear-gradient(120deg, #2c3e50, #3498db);
#             color: white;
#             text-align: center;
#             padding: 40px;
#         }
#         h1 {
#             font-size: 2.8em;
#             margin-bottom: 20px;
#         }
#         #camera {
#             border-radius: 15px;
#             box-shadow: 0 0 25px rgba(0,0,0,0.4);
#             margin-top: 20px;
#         }
#         #arrow {
#             font-size: 80px;
#             margin: 30px 0;
#             animation: float 1.5s ease-in-out infinite;
#         }
#         @keyframes float {
#             0%, 100% { transform: translateY(0); }
#             50% { transform: translateY(-10px); }
#         }
#         #result {
#             font-size: 24px;
#             margin-top: 20px;
#         }
#         button {
#             background-color: #1abc9c;
#             color: white;
#             border: none;
#             padding: 14px 28px;
#             font-size: 18px;
#             border-radius: 8px;
#             cursor: pointer;
#             margin-top: 25px;
#             transition: background 0.3s ease;
#         }
#         button:hover {
#             background-color: #16a085;
#         }
#     </style>
# </head>
# <body>
#     <h1>Smart Waste Sorting System</h1>
#     <video id="camera" width="480" height="360" autoplay muted></video>
#     <div id="result">Waiting for prediction...</div>
#     <div id="arrow">🔄</div>
#
#     <script>
#         const video = document.getElementById('camera');
#         const result = document.getElementById('result');
#         const arrow = document.getElementById('arrow');
#
#         navigator.mediaDevices.getUserMedia({ video: true })
#             .then(stream => video.srcObject = stream)
#             .catch(error => console.error('Camera error:', error));
#
#         function classifyFrame() {
#             const canvas = document.createElement('canvas');
#             canvas.width = video.videoWidth;
#             canvas.height = video.videoHeight;
#             canvas.getContext('2d').drawImage(video, 0, 0);
#             const imageData = canvas.toDataURL('image/jpeg');  // Send image as JPEG
#
#             console.log("Sending image data:", imageData);  // Debug log
#
#             fetch('/classify', {
#                 method: 'POST',
#                 headers: { 'Content-Type': 'application/json' },
#                 body: JSON.stringify({ image: imageData })
#             })
#             .then(response => {
#                 if (!response.ok) {
#                     throw new Error('Failed to classify image');
#                 }
#                 return response.json();
#             })
#             .then(data => {
#                 result.innerText = 'Detected: ' + data.category;
#                 switch (data.category.toLowerCase()) {
#                     case 'cardboard':
#                     case 'paper':
#                         arrow.innerText = '⬅️ Put in Compost Bin';
#                         break;
#                     case 'trash':
#                     case 'plastic':
#                         arrow.innerText = '⬇️ Put in Trash Bin';
#                         break;
#                     case 'metal':
#                     case 'glass':
#                         arrow.innerText = '➡️ Put in Metal Bin';
#                         break;
#                     default:
#                         arrow.innerText = '❓ Unknown';
#                 }
#             })
#             .catch(err => {
#                 result.innerText = 'Error: ' + err.message;
#                 arrow.innerText = '';
#             });
#         }
#
#         setInterval(classifyFrame, 3000);  // Classify every 3 seconds
#     </script>
# </body>
# </html>
# ''')
#
#
# # Classification route
# @app.route('/classify', methods=['POST'])
# def classify():
#     try:
#         data = request.get_json()
#         if 'image' not in data:
#             return jsonify({'error': 'No image received'}), 400
#
#         image_data = data['image'].split(',')[1]  # Remove base64 header part
#         file_bytes = np.frombuffer(base64.b64decode(image_data), np.uint8)
#         image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#
#         if image is None:
#             return jsonify({'error': 'Failed to decode image'}), 400
#
#         print("Image decoded successfully")  # Debug log
#
#         processed_image = preprocess_image(image)
#
#         print("Image preprocessed successfully")  # Debug log
#
#         prediction = model.predict(processed_image)
#         class_index = np.argmax(prediction)
#         category = labels[class_index]
#
#         print(f"Prediction: {category}")  # Debug log
#
#         return jsonify({'category': category})
#
#     except Exception as e:
#         print(f"Error occurred: {str(e)}")  # Detailed error log
#         return jsonify({'error': f'An error occurred: {str(e)}'}), 500
#
#
# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask, request, render_template_string, jsonify
# import numpy as np
# from tensorflow.keras.models import load_model
# import base64
# from PIL import Image
# import io
#
# app = Flask(__name__)
#
# # Load your trained model
# model = load_model("waste-classification-model.h5")
#
# # Preprocess image to match model input
# def preprocess_image(img_data):
#     img = Image.open(io.BytesIO(img_data))
#     img = img.resize((224, 224))
#     img_array = np.array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array = img_array / 255.0
#     return img_array
#
# # HTML and JS with animations and camera
# HTML_TEMPLATE = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Smart Waste Sorting</title>
#     <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
#     <style>
#         body {
#             font-family: 'Roboto', sans-serif;
#             margin: 0;
#             padding: 0;
#             background: linear-gradient(120deg, #2c3e50, #3498db);
#             color: #fff;
#             text-align: center;
#         }
#         header {
#             background: #1abc9c;
#             padding: 20px;
#             font-size: 28px;
#             font-weight: bold;
#             animation: slideDown 1s ease-out;
#         }
#         .container {
#             margin: 40px auto;
#             padding: 30px;
#             background: #ffffff10;
#             border-radius: 15px;
#             width: 80%;
#             max-width: 600px;
#             box-shadow: 0 4px 20px rgba(0,0,0,0.3);
#         }
#         video {
#             border-radius: 10px;
#             width: 100%;
#             max-width: 480px;
#         }
#         canvas { display: none; }
#         button {
#             margin-top: 20px;
#             padding: 14px 28px;
#             font-size: 18px;
#             background-color: #e67e22;
#             color: white;
#             border: none;
#             border-radius: 8px;
#             cursor: pointer;
#             transition: background 0.3s ease;
#         }
#         button:hover {
#             background-color: #d35400;
#         }
#         .result {
#             margin-top: 20px;
#             font-size: 20px;
#             background: #2ecc71;
#             padding: 10px;
#             border-radius: 10px;
#             animation: fadeIn 1s ease-in;
#         }
#         .arrow {
#             font-size: 64px;
#             margin-top: 20px;
#             animation: float 1.5s infinite ease-in-out;
#         }
#         @keyframes slideDown {
#             from { transform: translateY(-100px); opacity: 0; }
#             to { transform: translateY(0); opacity: 1; }
#         }
#         @keyframes fadeIn {
#             from { opacity: 0; }
#             to { opacity: 1; }
#         }
#         @keyframes float {
#             0%, 100% { transform: translateY(0); }
#             50% { transform: translateY(-10px); }
#         }
#     </style>
# </head>
# <body>
#
# <header>Smart Waste Sorting System</header>
#
# <div class="container">
#     <video id="video" autoplay></video><br>
#     <button onclick="captureAndClassify()">Capture & Classify</button>
#
#     <div class="result" id="result" style="display:none;">
#         <div id="category"></div>
#         <div class="arrow" id="arrow">🔄</div>
#     </div>
# </div>
#
# <canvas id="canvas"></canvas>
#
# <script>
#     const video = document.getElementById('video');
#     const canvas = document.getElementById('canvas');
#     const context = canvas.getContext('2d');
#     const resultDiv = document.getElementById('result');
#     const categoryDiv = document.getElementById('category');
#     const arrowDiv = document.getElementById('arrow');
#
#     navigator.mediaDevices.getUserMedia({ video: true })
#         .then(stream => video.srcObject = stream)
#         .catch(err => console.error('Camera error:', err));
#
#     function captureAndClassify() {
#         canvas.width = video.videoWidth;
#         canvas.height = video.videoHeight;
#         context.drawImage(video, 0, 0);
#         const imageData = canvas.toDataURL('image/jpeg');
#
#         fetch('/classify', {
#             method: 'POST',
#             headers: { 'Content-Type': 'application/json' },
#             body: JSON.stringify({ image: imageData })
#         })
#         .then(response => response.json())
#         .then(data => {
#             resultDiv.style.display = 'block';
#
#             const probs = data;
#             const maxLabel = Object.keys(probs).reduce((a, b) => probs[a] > probs[b] ? a : b);
#
#             categoryDiv.innerText = `Detected: ${maxLabel.toUpperCase()}`;
#             if (maxLabel === "organic") {
#                 arrowDiv.innerText = "⬅️ Put in Compost Bin";
#             } else if (maxLabel === "trash") {
#                 arrowDiv.innerText = "⬇️ Put in Trash Bin";
#             } else if (maxLabel === "metal") {
#                 arrowDiv.innerText = "➡️ Put in Metal Bin";
#             } else {
#                 arrowDiv.innerText = "❓ Unknown";
#             }
#         })
#         .catch(err => {
#             categoryDiv.innerText = 'Error: ' + err;
#             arrowDiv.innerText = '';
#         });
#     }
# </script>
#
# </body>
# </html>
# """
#
# @app.route('/')
# def index():
#     return render_template_string(HTML_TEMPLATE)
#
# @app.route('/classify', methods=['POST'])
# def classify():
#     try:
#         img_data = request.json['image'].split(',')[1]
#         img_data = base64.b64decode(img_data)
#         img_array = preprocess_image(img_data)
#         prediction = model.predict(img_array)
#
#         return jsonify({
#             "organic": float(prediction[0][0]),
#             "trash": float(prediction[0][1]),
#             "metal": float(prediction[0][2])
#         })
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
#
# if __name__ == '__main__':
#     app.run(debug=True)
#




# from flask import Flask, request, render_template_string, jsonify
# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import io
# from PIL import Image
# import base64
#
# app = Flask(__name__)
#
# # Load the trained model
# model = load_model("waste-classification-model.h5")
# labels = ["Compost", "Trash", "Metal"]
#
# # Preprocess the image
# def preprocess_image(img_data):
#     img = Image.open(io.BytesIO(img_data))
#     img = img.resize((224, 224))
#     img_array = np.array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array = img_array / 255.0
#     return img_array
#
# # HTML with animations and sound
# HTML_TEMPLATE = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>JET Waste AI Sorting Tool</title>
#     <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
#     <style>
#         body {
#             font-family: 'Roboto', sans-serif;
#             background: linear-gradient(to right, #1e3c72, #2a5298);
#             margin: 0;
#             padding: 0;
#             color: white;
#             text-align: center;
#             animation: fadeIn 2s ease-in;
#         }
#         header {
#             background: #0d47a1;
#             padding: 20px;
#             font-size: 2em;
#             font-weight: bold;
#             box-shadow: 0 2px 10px rgba(0,0,0,0.3);
#         }
#         #camera-container {
#             margin-top: 30px;
#         }
#         video {
#             border: 5px solid #0d47a1;
#             border-radius: 15px;
#             box-shadow: 0 10px 30px rgba(0,0,0,0.5);
#         }
#         #arrow {
#             font-size: 60px;
#             margin-top: 20px;
#             animation: float 2s infinite;
#         }
#         #result {
#             margin-top: 20px;
#             font-size: 24px;
#         }
#         @keyframes fadeIn {
#             from { opacity: 0; transform: translateY(-20px); }
#             to { opacity: 1; transform: translateY(0); }
#         }
#         @keyframes float {
#             0%, 100% { transform: translateY(0); }
#             50% { transform: translateY(-10px); }
#         }
#     </style>
# </head>
# <body>
#     <header>JET Waste AI Sorting Tool</header>
#     <div id="camera-container">
#         <video id="video" width="480" height="360" autoplay muted></video>
#         <div id="result">Waiting for prediction...</div>
#         <div id="arrow">🔄</div>
#     </div>
#     <audio id="alert-sound" src="https://www.soundjay.com/buttons/sounds/beep-07.mp3"></audio>
#
#     <canvas id="canvas" style="display:none;"></canvas>
#     <script>
#         const video = document.getElementById('video');
#         const canvas = document.getElementById('canvas');
#         const result = document.getElementById('result');
#         const arrow = document.getElementById('arrow');
#         const alertSound = document.getElementById('alert-sound');
#         const context = canvas.getContext('2d');
#
#         navigator.mediaDevices.getUserMedia({ video: true })
#             .then(stream => video.srcObject = stream)
#             .catch(error => console.error('Camera error:', error));
#
#         function classifyImage() {
#             canvas.width = video.videoWidth;
#             canvas.height = video.videoHeight;
#             context.drawImage(video, 0, 0);
#             const imageData = canvas.toDataURL('image/jpeg');
#
#             fetch('/classify', {
#                 method: 'POST',
#                 headers: { 'Content-Type': 'application/json' },
#                 body: JSON.stringify({ image: imageData })
#             })
#             .then(response => response.json())
#             .then(data => {
#                 alertSound.play();
#                 result.innerText = 'Detected: ' + data.category;
#                 switch (data.category) {
#                     case 'Compost':
#                         arrow.innerText = '⬅️ Put in Compost Bin';
#                         break;
#                     case 'Trash':
#                         arrow.innerText = '⬇️ Put in Trash Bin';
#                         break;
#                     case 'Metal':
#                         arrow.innerText = '➡️ Put in Metal Bin';
#                         break;
#                     default:
#                         arrow.innerText = '❓ Unknown';
#                 }
#             })
#             .catch(err => {
#                 result.innerText = 'Error: ' + err;
#                 arrow.innerText = '';
#             });
#         }
#
#         setInterval(classifyImage, 1000);
#     </script>
# </body>
# </html>
# """
#
# @app.route('/')
# def home():
#     return render_template_string(HTML_TEMPLATE)
#
# @app.route('/classify', methods=['POST'])
# def classify():
#     try:
#         img_data = request.json['image'].split(',')[1]
#         img_bytes = base64.b64decode(img_data)
#         img_array = preprocess_image(img_bytes)
#         prediction = model.predict(img_array)
#         category = labels[np.argmax(prediction)]
#         return jsonify({'category': category})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
#
# if __name__ == '__main__':
#     app.run(debug=True)



#
# from flask import Flask, request, render_template_string, jsonify
# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import io
# from PIL import Image
# import base64
#
# app = Flask(__name__)
#
# # Load the trained model
# model = load_model("waste-classification-model.h5")
#
# # ✅ Updated to match 6-class output
# labels = ["Cardboard", "Glass", "Metal", "Paper", "Plastic", "Trash"]
#
# # Preprocess the image
# def preprocess_image(img_data):
#     img = Image.open(io.BytesIO(img_data))
#     img = img.resize((32, 32))  # ✅ Match model input size
#     img_array = np.array(img)
#     if img_array.shape[-1] == 4:  # Handle PNG with alpha
#         img_array = img_array[..., :3]
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array = img_array / 255.0
#     return img_array
#
# # HTML UI
# HTML_TEMPLATE = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>JET Waste AI Sorting Tool</title>
#     <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
#     <style>
#         body {
#             font-family: 'Roboto', sans-serif;
#             background: linear-gradient(to right, #1e3c72, #2a5298);
#             margin: 0;
#             padding: 0;
#             color: white;
#             text-align: center;
#             animation: fadeIn 2s ease-in;
#         }
#         header {
#             background: #0d47a1;
#             padding: 20px;
#             font-size: 2em;
#             font-weight: bold;
#             box-shadow: 0 2px 10px rgba(0,0,0,0.3);
#         }
#         #camera-container {
#             margin-top: 30px;
#         }
#         video {
#             border: 5px solid #0d47a1;
#             border-radius: 15px;
#             box-shadow: 0 10px 30px rgba(0,0,0,0.5);
#         }
#         #arrow {
#             font-size: 60px;
#             margin-top: 20px;
#             animation: float 2s infinite;
#         }
#         #result {
#             margin-top: 20px;
#             font-size: 24px;
#         }
#         @keyframes fadeIn {
#             from { opacity: 0; transform: translateY(-20px); }
#             to { opacity: 1; transform: translateY(0); }
#         }
#         @keyframes float {
#             0%, 100% { transform: translateY(0); }
#             50% { transform: translateY(-10px); }
#         }
#     </style>
# </head>
# <body>
#     <header>JET Waste AI Sorting Tool</header>
#     <div id="camera-container">
#         <video id="video" width="480" height="360" autoplay muted></video>
#         <div id="result">Waiting for prediction...</div>
#         <div id="arrow">🔄</div>
#     </div>
#     <audio id="alert-sound" src="https://www.soundjay.com/buttons/sounds/beep-07.mp3"></audio>
#
#     <canvas id="canvas" style="display:none;"></canvas>
#     <script>
#         const video = document.getElementById('video');
#         const canvas = document.getElementById('canvas');
#         const result = document.getElementById('result');
#         const arrow = document.getElementById('arrow');
#         const alertSound = document.getElementById('alert-sound');
#         const context = canvas.getContext('2d');
#
#         navigator.mediaDevices.getUserMedia({ video: true })
#             .then(stream => video.srcObject = stream)
#             .catch(error => console.error('Camera error:', error));
#
#         function classifyImage() {
#             canvas.width = video.videoWidth;
#             canvas.height = video.videoHeight;
#             context.drawImage(video, 0, 0);
#             const imageData = canvas.toDataURL('image/jpeg');
#
#             fetch('/classify', {
#                 method: 'POST',
#                 headers: { 'Content-Type': 'application/json' },
#                 body: JSON.stringify({ image: imageData })
#             })
#             .then(response => response.json())
#             .then(data => {
#                 alertSound.play();
#                 result.innerText = 'Detected: ' + data.category;
#
#                 const arrows = {
#                     "Cardboard": "⬅️ Put in Cardboard Bin",
#                     "Glass": "⬅️ Put in Glass Bin",
#                     "Metal": "➡️ Put in Metal Bin",
#                     "Paper": "⬆️ Put in Paper Bin",
#                     "Plastic": "⬇️ Put in Plastic Bin",
#                     "Trash": "🗑️ Put in Trash Bin"
#                 };
#
#                 arrow.innerText = arrows[data.category] || '❓ Unknown';
#             })
#             .catch(err => {
#                 result.innerText = 'Error: ' + err;
#                 arrow.innerText = '';
#             });
#         }
#
#         setInterval(classifyImage, 1000);
#     </script>
# </body>
# </html>
# """
#
# @app.route('/')
# def home():
#     return render_template_string(HTML_TEMPLATE)
#
# @app.route('/classify', methods=['POST'])
# def classify():
#     try:
#         img_data = request.json['image'].split(',')[1]
#         img_bytes = base64.b64decode(img_data)
#         img_array = preprocess_image(img_bytes)
#         prediction = model.predict(img_array)
#         category = labels[np.argmax(prediction)]
#         return jsonify({'category': category})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
#
# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, render_template_string, jsonify
# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import io
# from PIL import Image
# import base64
#
# app = Flask(__name__)
#
# # Load the trained model
# model = load_model("waste-classification-model.h5")
# labels = ["Compost", "Trash", "Metal"]
#
# def preprocess_image(img_data):
#     img = Image.open(io.BytesIO(img_data)).convert("RGB")
#     img = img.resize((32, 32))  # Match model input
#     img_array = np.array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array = img_array / 255.0
#     return img_array
#
# HTML_TEMPLATE = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>JET Waste AI Sorting Tool</title>
#     <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap" rel="stylesheet">
#     <style>
#         body {
#             font-family: 'Roboto', sans-serif;
#             background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
#             color: white;
#             text-align: center;
#             margin: 0;
#             padding: 0;
#         }
#         header {
#             padding: 30px;
#             font-size: 2.5em;
#             background-color: #0d47a1;
#             box-shadow: 0 4px 10px rgba(0,0,0,0.3);
#         }
#         video {
#             border: 6px solid #ffffff33;
#             border-radius: 15px;
#             box-shadow: 0 12px 35px rgba(0, 0, 0, 0.5);
#             margin-top: 20px;
#         }
#         #arrow {
#             font-size: 60px;
#             margin-top: 20px;
#             opacity: 0;
#             transition: all 0.5s ease;
#         }
#         #arrow.show {
#             opacity: 1;
#             animation: moveArrow 1.2s ease-in-out infinite;
#         }
#         #result {
#             font-size: 1.5em;
#             margin-top: 10px;
#         }
#         @keyframes moveArrow {
#             0%, 100% { transform: translateY(0); }
#             50% { transform: translateY(-12px); }
#         }
#     </style>
# </head>
# <body>
#     <header>JET Waste AI Sorting Tool</header>
#     <div>
#         <video id="video" width="480" height="360" autoplay muted></video>
#         <div id="result">Loading...</div>
#         <div id="arrow">🔄</div>
#     </div>
#
#     <!-- Sound effects -->
#     <audio id="compost-sound" src="https://www.soundjay.com/buttons/sounds/button-30.mp3"></audio>
#     <audio id="trash-sound" src="https://www.soundjay.com/buttons/sounds/button-10.mp3"></audio>
#     <audio id="metal-sound" src="https://www.soundjay.com/buttons/sounds/button-16.mp3"></audio>
#
#     <canvas id="canvas" style="display:none;"></canvas>
#
#     <script>
#         const video = document.getElementById('video');
#         const canvas = document.getElementById('canvas');
#         const result = document.getElementById('result');
#         const arrow = document.getElementById('arrow');
#
#         const compostSound = document.getElementById('compost-sound');
#         const trashSound = document.getElementById('trash-sound');
#         const metalSound = document.getElementById('metal-sound');
#
#         const context = canvas.getContext('2d');
#
#         navigator.mediaDevices.getUserMedia({ video: true })
#             .then(stream => video.srcObject = stream)
#             .catch(error => console.error('Camera error:', error));
#
#         function classifyImage() {
#             canvas.width = video.videoWidth;
#             canvas.height = video.videoHeight;
#             context.drawImage(video, 0, 0);
#             const imageData = canvas.toDataURL('image/jpeg');
#
#             fetch('/classify', {
#                 method: 'POST',
#                 headers: { 'Content-Type': 'application/json' },
#                 body: JSON.stringify({ image: imageData })
#             })
#             .then(response => response.json())
#             .then(data => {
#                 result.innerText = 'Detected: ' + data.category;
#                 arrow.classList.add('show');
#
#                 switch (data.category) {
#                     case 'Compost':
#                         arrow.innerText = '⬅️ Compost Bin';
#                         compostSound.play();
#                         break;
#                     case 'Trash':
#                         arrow.innerText = '⬇️ Trash Bin';
#                         trashSound.play();
#                         break;
#                     case 'Metal':
#                         arrow.innerText = '➡️ Metal Bin';
#                         metalSound.play();
#                         break;
#                     default:
#                         arrow.innerText = '❓ Unknown';
#                         arrow.classList.remove('show');
#                 }
#             })
#             .catch(err => {
#                 result.innerText = 'Error: ' + err;
#                 arrow.innerText = '';
#             });
#         }
#
#         setInterval(classifyImage, 1000);
#     </script>
# </body>
# </html>
# """
#
# @app.route('/')
# def home():
#     return render_template_string(HTML_TEMPLATE)
#
# @app.route('/classify', methods=['POST'])
# def classify():
#     try:
#         img_data = request.json['image'].split(',')[1]
#         img_bytes = base64.b64decode(img_data)
#         img_array = preprocess_image(img_bytes)
#         prediction = model.predict(img_array)
#         category = labels[np.argmax(prediction)]
#         return jsonify({'category': category})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
#
# if __name__ == '__main__':
#     app.run(debug=True)

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


