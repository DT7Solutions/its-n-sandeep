# Generated by Django 4.1.3 on 2022-11-18 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_about_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(default='heading', max_length=25)),
                ('Description', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
