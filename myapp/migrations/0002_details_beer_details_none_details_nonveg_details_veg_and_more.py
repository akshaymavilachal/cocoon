# Generated by Django 4.0 on 2021-12-29 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='beer',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='details',
            name='none',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='details',
            name='nonveg',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='details',
            name='veg',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='details',
            name='whisky',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='details',
            name='wine',
            field=models.CharField(default='', max_length=20),
        ),
    ]
