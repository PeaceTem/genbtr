# Generated by Django 3.2.9 on 2022-07-16 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leak', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='leak',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]