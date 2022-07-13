from django.db import models
from django.contrib.auth.models import User
from leak.models import Leak, Category, Subcategory

from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField
# Create your models here.

"""
Search the web for django model draft
"""


class DraftLeak(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='draft', auto_created=True)
    title = models.CharField(max_length=200, verbose_name=_('title'), null=True, blank=True)
    story = RichTextField(verbose_name=_('story'), null=True, blank=True) # try to change the verbose name and see what will happen 
    date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='leak_draft_category')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True, related_name='leak_draft_subcategory')

    def __str__(self):
        return f"{self.title}"

