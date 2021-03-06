from django.contrib.auth.forms import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')