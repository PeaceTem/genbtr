from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _


"""
widgets = forms.Textarea, forms.TextInput(attrs={'class':'input-class'}), forms.Select
required = bool

add multiple choice field for category in subcategory page 256

"""

class CustomUserForm(UserCreationForm):
    first_name = forms.CharField(label=_("First Name"), max_length=100)
    last_name = forms.CharField(label=_("Last Name"), max_length=100)
    email = forms.EmailField(label=_("Email")) # use charfield with type = email