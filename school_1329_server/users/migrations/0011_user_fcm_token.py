# Generated by Django 2.0 on 2018-02-23 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180213_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fcm_token',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
