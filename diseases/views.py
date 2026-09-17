from django.shortcuts import render, get_object_or_404
from .models import Disease


def disease_list(request):
    diseases = Disease.objects.filter(is_healthy=False)
    crop_filter = request.GET.get("crop")
    if crop_filter:
        diseases = diseases.filter(crop__iexact=crop_filter)
    crops = Disease.objects.values_list("crop", flat=True).distinct()
    return render(request, "diseases/list.html", {"diseases": diseases, "crops": crops})


def disease_detail(request, pk):
    disease = get_object_or_404(Disease, pk=pk)
    return render(request, "diseases/detail.html", {"disease": disease})





