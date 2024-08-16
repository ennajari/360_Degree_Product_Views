from flask import Flask, render_template, jsonify
import os
from models.generate_3d_model import generate_3d_model
from models.analyze_apple import analyze_apple

app = Flask(__name__)

@app.route('/')
def index():
    image_folder = os.path.join('static', 'data', 'images')
    images = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg')])
    
    # Générer le modèle 3D (simulation)
    model_3d = generate_3d_model(images)
    
    # Analyser la première image
    first_image_path = os.path.join(image_folder, images[0])
    analysis = analyze_apple(first_image_path)
    
    return render_template('index.html', images=images, analysis=analysis)

@app.route('/api/analysis')
def get_analysis():
    image_folder = os.path.join('static', 'data', 'images')
    images = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg')])
    first_image_path = os.path.join(image_folder, images[0])
    analysis = analyze_apple(first_image_path)
    return jsonify(analysis)

if __name__ == '__main__':
    app.run(debug=True)
