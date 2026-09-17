from django.urls import path
from . import views

app_name = "detection"

urlpatterns = [
    path("upload/", views.upload_image, name="upload_image"),
    path("result/<int:pk>/", views.view_result, name="view_result"),
    path("history/", views.prediction_history, name="prediction_history"),
]

