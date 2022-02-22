# Generated by Django 4.0 on 2022-02-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/sliders')),
                ('discount_deal', models.CharField(choices=[('HOT DEALS', 'Hot Deals'), ('NEW ARRIVALS', 'New Arrivals')], max_length=100)),
                ('sale', models.IntegerField()),
                ('brand_name', models.CharField(max_length=100)),
                ('discount', models.IntegerField()),
                ('link', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Sliders',
            },
        ),
    ]
