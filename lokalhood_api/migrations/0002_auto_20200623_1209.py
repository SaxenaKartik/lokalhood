# Generated by Django 3.0.7 on 2020-06-23 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lokalhood_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Request',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
