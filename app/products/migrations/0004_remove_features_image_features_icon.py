# Generated by Django 4.0 on 2022-02-24 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='features',
            name='image',
        ),
        migrations.AddField(
            model_name='features',
            name='icon',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
