import numpy as np
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

from .ml.model_loader import get_model, CLASS_LABELS
from diseases.models import Disease

IMAGE_SIZE = (224, 224)  # MobileNetV2 default input size


def preprocess_image(image_file):
    """Convert an uploaded image file into a MobileNet-ready array."""
    image_file.seek(0)  # reset read position — Django's form validation already read this file once
    img = Image.open(image_file).convert("RGB")
    img = img.resize(IMAGE_SIZE)
    array = np.array(img)
    array = preprocess_input(array)
    return np.expand_dims(array, axis=0)

def predict_disease(image_file):
    """
    Run the uploaded image through the trained model.
    Returns (Disease instance or None, confidence float).
    """
    model = get_model()
    processed = preprocess_image(image_file)

    predictions = model.predict(processed)[0]
    predicted_index = int(np.argmax(predictions))
    confidence = float(predictions[predicted_index])
    label = CLASS_LABELS[predicted_index]

    disease = Disease.objects.filter(label=label).first()
    return disease, confidence


  