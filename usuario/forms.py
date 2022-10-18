from django.forms import ModelForm, Select
from django.contrib.auth.models import User

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        exclude = ['groups', 'is_active', 'is_superuser', 'is_staff', 'date_joined']
