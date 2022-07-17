from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from leak.models import Subcategory


from src.utils import LANGUAGES
# Create your models here.
"""

add email field to usercreationform
Create a list of all languages

"""
# add each profile to drafts
class Profile(models.Model):
    SEX =(
        ('male', _('male')),
        ('female', _('female')),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', auto_created=True)
    picture = models.ImageField(upload_to='genz/profile_picture/', null=True, blank=True, verbose_name=_("Picture"))
    first_name = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Last Name"))
    middle_name = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Middle Name"))
    bio = models.TextField(max_length=1000, null=True, blank=True, verbose_name=_("Biography"))
    gender = models.CharField(max_length=10, choices=SEX, null=True, blank=True, verbose_name=_("Gender"))
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=_("Date Of Birth"))
    state_of_residence = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("state Of Residence"))
    state_of_origin = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("State Of Origin"))
    nationality = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Nationlity"))
    language1 = models.CharField(max_length=100, choices=LANGUAGES, null=True, blank=True, verbose_name=_("First Language"))
    language2 = models.CharField(max_length=100, choices=LANGUAGES, null=True, blank=True, verbose_name=_("Second Language"))
    date_updated = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.user}"