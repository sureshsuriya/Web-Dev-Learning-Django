# Generated by Django 4.2.3 on 2023-08-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newdb',
            name='g',
            field=models.CharField(default='Male', max_length=15),
        ),
    ]
