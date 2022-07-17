



from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

from django.core.exceptions import ValidationError


"""
widgets = forms.Textarea, forms.TextInput(attrs={'class':'input-class'}), forms.Select
required = bool

add multiple choice field for category in subcategory page 256


FilePathField

"""

class CustomUserForm(UserCreationForm):
    first_name = forms.CharField(label=_("First Name"), max_length=100)
    last_name = forms.CharField(label=_("Last Name"), max_length=100)
    email = forms.EmailField(label=_("Email"))

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email):
            raise ValidationError(_("Email has already been used by another user"), code='invalid')
        return self.cleaned_data
