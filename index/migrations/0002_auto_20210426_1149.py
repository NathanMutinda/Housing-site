# Generated by Django 3.1.5 on 2021-04-26 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='H_name',
            new_name='h_name',
        ),
    ]
