# Generated by Django 2.0.2 on 2020-08-20 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='description',
            new_name='name',
        ),
    ]
