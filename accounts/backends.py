from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User 
from django.shortcuts import reverse

class CustomUserBackend(ModelBackend):

    def user_can_access_dashboard(self, user):
        # Implement logic to check the user's role and return the appropriate dashboard URL
        if user.is_authenticated:
            if user.is_company:
                return reverse('employer_dashboard')
            elif user.is_jobseeker:
                return reverse('jobseeker_dashboard')
        return reverse('default_dashboard')  # Default dashboard URL

    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
