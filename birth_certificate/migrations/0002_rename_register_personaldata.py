# Generated by Django 4.0.3 on 2022-05-14 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birth_certificate', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='PersonalData',
        ),
    ]