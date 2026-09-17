from django.contrib import admin
from .models import Disease


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ["name", "crop", "label", "is_healthy", "updated_at"]
    list_filter = ["crop", "is_healthy"]
    search_fields = ["name", "crop", "label"]

  