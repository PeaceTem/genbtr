# Generated by Django 3.2.9 on 2022-07-08 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leak', '0002_auto_20220708_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leak',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='leak.category'),
        ),
    ]