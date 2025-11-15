from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

model = joblib.load('savedmodel.pth')

def prepare_image(file):
    img = Image.open(file).convert('L')
    img = img.resize((64, 64))
    arr = np.array(img).reshape(1, -1)
    arr = arr / 255.0
    return arr

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    filename = None
    if request.method == 'POST':
        if "file" not in request.files or request.files["file"].filename == "":
            return render_template("index.html", prediction="No file selected", filename=None)
        file = request.files["file"]
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        data = prepare_image(filepath)
        pred = model.predict(data)
        prediction = pred[0]
        filename = file.filename
    return render_template('index.html', prediction=prediction, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)