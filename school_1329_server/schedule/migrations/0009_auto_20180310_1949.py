# Generated by Django 2.0 on 2018-03-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_auto_20180309_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulelesson',
            name='place',
            field=models.CharField(blank=True, max_length=200, verbose_name='Место проведения'),
        ),
    ]