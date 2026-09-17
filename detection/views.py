from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ImageUploadForm
from .models import Prediction
from .services import predict_disease


def upload_image(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            prediction = form.save(commit=False)
            if request.user.is_authenticated:
                prediction.user = request.user

            disease, confidence = predict_disease(request.FILES["image"])
            prediction.disease = disease
            prediction.confidence = confidence
            prediction.save()

            return redirect("detection:view_result", pk=prediction.pk)
    else:
        form = ImageUploadForm()
    return render(request, "detection/upload.html", {"form": form})


def view_result(request, pk):
    prediction = get_object_or_404(Prediction, pk=pk)
    return render(request, "detection/result.html", {"prediction": prediction})


@login_required
def prediction_history(request):
    predictions = request.user.predictions.select_related("disease").order_by("-created_at")
    return render(request, "detection/history.html", {"predictions": predictions})



  