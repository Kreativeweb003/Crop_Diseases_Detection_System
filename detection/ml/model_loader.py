import os
from django.conf import settings
from tensorflow.keras.models import load_model

_model = None  # module-level cache so the model loads once, not per-request

MODEL_PATH = os.path.join(settings.BASE_DIR, "detection", "ml", "crop_disease_mobilenet.h5")

# Must match the order of class labels used during training
CLASS_LABELS = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy",
]


def get_model():
    global _model
    if _model is None:
        _model = load_model(MODEL_PATH)
    return _model


