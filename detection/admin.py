from django.contrib import admin
from .models import Prediction


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "disease", "confidence", "created_at"]
    list_filter = ["disease", "created_at"]
    search_fields = ["user__username"]



