# Generated by Django 4.0 on 2022-02-24 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerlower',
            name='position',
            field=models.CharField(blank=True, choices=[('TOP', 'Top'), ('MIDDLE', 'Middle'), ('LOWER', 'Lower')], max_length=10, null=True),
        ),
    ]
