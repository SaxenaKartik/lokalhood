# Generated by Django 3.0.7 on 2020-07-11 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lokalhood_api', '0003_request_shop_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lokalhood_api.Shop'),
        ),
    ]
