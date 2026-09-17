from django.db import models
from django.contrib.auth.models import User
from diseases.models import Disease


class Prediction(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="predictions",
        null=True, blank=True  # allow anonymous/guest predictions if desired
    )
    image = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    disease = models.ForeignKey(
        Disease, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="predictions"
    )
    confidence = models.FloatField(help_text="Model confidence score, 0-1")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "detection_prediction"
        ordering = ["-created_at"]

    def __str__(self):
        disease_name = self.disease.name if self.disease else "Unknown"
        return f"{disease_name} ({self.confidence:.0%}) - {self.created_at:%Y-%m-%d}"




