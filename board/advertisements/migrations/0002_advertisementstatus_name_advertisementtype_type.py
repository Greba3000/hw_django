# Generated by Django 4.0 on 2022-03-27 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisementstatus',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='advertisementtype',
            name='type',
            field=models.CharField(default='', max_length=100),
        ),
    ]
