# Generated by Django 4.2.3 on 2023-08-08 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('passw', models.CharField(max_length=15)),
                ('gend', models.CharField(default='Male', max_length=15)),
                ('cou', models.CharField(max_length=14)),
                ('num', models.CharField(max_length=10)),
                ('img', models.ImageField(default=None, upload_to='images/')),
            ],
        ),
    ]
