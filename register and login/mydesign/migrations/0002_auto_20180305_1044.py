# Generated by Django 2.0.2 on 2018-03-05 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydesign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='mark',
            field=models.FloatField(max_length=4, verbose_name='评分'),
        ),
    ]
