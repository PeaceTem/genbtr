# Generated by Django 3.2.9 on 2022-07-12 08:36

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leak', '0008_subcategory_creator'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DraftLeak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='title')),
                ('story', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='story')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leak_draft_category', to='leak.category')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leak_draft_subcategory', to='leak.subcategory')),
                ('user', models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]