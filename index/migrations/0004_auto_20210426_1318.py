# Generated by Django 3.1.5 on 2021-04-26 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_house_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='picture',
            field=models.ImageField(blank=True, default="{% static 'images/IMG_20210418_160459_5.jpg' %}", null=True, upload_to='images'),
        ),
    ]
