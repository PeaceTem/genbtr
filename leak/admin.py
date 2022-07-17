from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Image)
admin.site.register(Audio)

# class FileAdminUploadForm(forms.ModelForm):
#     file = forms.FileField(widget=CKEditorUploadingWidget())
#     class Meta:
#         model = File
#         fields = '__all__'

class FileAdmin(admin.ModelAdmin):
    # form = FileAdminUploadForm
    # list_display=("title", "body")
    # prepopulated_fields={"slug": ("title",)}
    pass
# admin.site.register(File, FileAdmin)
admin.site.register(File)

admin.site.register(Video)
admin.site.register(Reply)
admin.site.register(Comment)
admin.site.register(Leak)
admin.site.register(Constitution)


