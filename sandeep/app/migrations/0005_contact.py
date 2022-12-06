# Generated by Django 4.1.3 on 2022-12-06 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default='heading', max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.CharField(max_length=200)),
            ],
        ),
    ]