from django.urls import path
from . import views

app_name = "diseases"

urlpatterns = [
    path("", views.disease_list, name="disease_list"),
    path("<int:pk>/", views.disease_detail, name="disease_detail"),
]