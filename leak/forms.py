from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget

from django.utils.text import slugify


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('title', 'description')

    def clean(self):
        title = self.cleaned_data.get('title')
        self.cleaned_data['slug'] = slugify(title)
        return self.cleaned_data


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


"""
AutoSlugfield
"""

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ('title', 'description', 'language')

    def clean(self):
        title = self.cleaned_data.get('title')
        self.cleaned_data['slug'] = slugify(title)
        return self.cleaned_data


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class ConstitutionForm(forms.ModelForm):
    class Meta:
        model = Constitution
        fields = ('law',)


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = '__all__'


class AudioForm(forms.ModelForm):

    class Meta:
        model = Audio
        fields = '__all__'




class FileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = '__all__'




class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = '__all__'


class ReplyForm(forms.ModelForm):
    reply = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Reply
        fields = ('reply',)




class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Comment
        fields = ('comment',)



class LeakForm(forms.ModelForm):

    class Meta:
        model = Leak
        fields = ('title', 'story')

    def clean(self):
        title = self.cleaned_data.get('title')
        self.cleaned_data['slug'] = slugify(title)
        return self.cleaned_data


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

