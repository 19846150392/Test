# Generated by Django 2.0.2 on 2018-03-06 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mydesign', '0005_auto_20180305_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visited',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mydesign.Movie')),
                ('u', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mydesign.User')),
            ],
        ),
    ]