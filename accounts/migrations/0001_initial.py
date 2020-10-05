# Generated by Django 2.0.2 on 2020-08-16 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=200)),
                ('address3', models.CharField(max_length=200)),
                ('mobilenumber', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=50)),
            ],
        ),
    ]
