from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .mixins import StyleFormMixin


class SignupForm(StyleFormMixin, UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    class Meta:
        model = CustomUser
        fields = ('email', 'avatar')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'avatar')

