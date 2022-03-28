# Generated by Django 4.0 on 2022-03-27 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_advertisementstatus_name_advertisementtype_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('tel', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AdvertisementHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.FloatField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements.advertisementstatus', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements.advertisementtype', verbose_name='Тип объявления'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements.advertisementauthor', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='heading',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements.advertisementheading', verbose_name='Рубрика'),
        ),
    ]
