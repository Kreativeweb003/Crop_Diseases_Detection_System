import os
from django.conf import settings
from tensorflow.keras.models import load_model

_model = None  # module-level cache so the model loads once, not per-request

MODEL_PATH = os.path.join(settings.BASE_DIR, "detection", "ml", "crop_disease_mobilenet.h5")

# Must match the order of class labels used during training
CLASS_LABELS = [
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___healthy",
    # add the rest of your trained classes here, in the exact training order
]


def get_model():
    global _model
    if _model is None:
        _model = load_model(MODEL_PATH)
    return _model


