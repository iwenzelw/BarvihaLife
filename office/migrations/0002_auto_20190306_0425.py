# Generated by Django 2.1.7 on 2019-03-06 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='tittle',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='room',
            name='titttle',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
