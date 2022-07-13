from django import forms

from .models import *

class DraftLeakForm(forms.ModelForm):

    class Meta:
        model = DraftLeak
        fields = ('title', 'story')