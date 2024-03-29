# Generated by Django 3.2.9 on 2022-07-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leak', '0003_subcategory_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='leak',
            name='shares',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leak',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
