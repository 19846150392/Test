# Generated by Django 3.0.8 on 2020-07-30 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydesign', '0012_auto_20180307_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=255, verbose_name='导演'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_link',
            field=models.CharField(max_length=255, verbose_name='Imdb链接'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=255, verbose_name='视频名称'),
        ),
    ]
