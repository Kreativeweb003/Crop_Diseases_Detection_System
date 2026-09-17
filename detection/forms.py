from django import forms
from .models import Prediction


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ["image"]
        widgets = {
            "image": forms.ClearableFileInput(attrs={"accept": "image/*"})
        }

    def clean_image(self):
        image = self.cleaned_data["image"]
        if image.size > 5 * 1024 * 1024:  # 5MB limit
            raise forms.ValidationError("Image file too large (max 5MB).")
        valid_extensions = [".jpg", ".jpeg", ".png"]
        if not any(image.name.lower().endswith(ext) for ext in valid_extensions):
            raise forms.ValidationError("Unsupported file type. Use JPG or PNG.")
        return image



