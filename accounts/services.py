from django.contrib.auth.models import User
from .models import Profile


def create_user_with_profile(form):
    """Create a User and an empty linked Profile from a valid RegistrationForm."""
    user = form.save()
    Profile.objects.create(user=user)
    return user


def get_user_prediction_history(user):
    """Return this user's past predictions, most recent first."""
    return user.predictions.select_related("disease").order_by("-created_at")




