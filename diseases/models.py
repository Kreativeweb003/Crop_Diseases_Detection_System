from django.db import models


class Disease(models.Model):
    name = models.CharField(max_length=100)                      # human-readable, e.g. "Early Blight"
    crop = models.CharField(max_length=50)                       # e.g. "Tomato"
    label = models.CharField(max_length=100, unique=True)         # must match training class name exactly,
                                                                    # e.g. "Tomato___Early_blight"
    is_healthy = models.BooleanField(default=False)               # True for "healthy" classes
    symptoms = models.TextField(blank=True)
    causes = models.TextField(blank=True)
    treatment = models.TextField(blank=True, help_text="Recommended management/treatment steps")
    image = models.ImageField(upload_to="diseases/", blank=True, null=True)  # reference/example image
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "diseases_disease"
        ordering = ["crop", "name"]
        verbose_name_plural = "diseases"

    def __str__(self):
        return f"{self.crop} - {self.name}"



