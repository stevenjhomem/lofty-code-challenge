# Generated by Django 4.1.7 on 2023-03-13 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DogImages',
            new_name='DogImageSet',
        ),
    ]