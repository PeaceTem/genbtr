from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget




class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('title', 'description')



class SubcategoryForm(forms.ModelForm):

    class Meta:
        model = Subcategory
        fields = ('title','description')


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

