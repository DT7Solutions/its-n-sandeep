# Generated by Django 4.1.3 on 2022-11-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='Description',
            field=models.CharField(max_length=2000),
        ),
    ]
