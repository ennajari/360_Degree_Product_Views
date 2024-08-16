import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
import numpy as np

model = MobileNetV2(weights='imagenet', include_top=True)

def analyze_apple(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = tf.keras.applications.mobilenet_v2.preprocess_input(x)
    
    predictions = model.predict(x)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]
    
    # Simuler l'analyse spécifique à la pomme
    color = "red" if "red" in img_path else "green"
    shape = "round"
    size = "medium"
    
    return {
        "color": color,
        "shape": shape,
        "estimated_size": size,
        "top_predictions": [
            {"class": class_name, "probability": float(score)} 
            for _, class_name, score in decoded_predictions
        ]
    }
