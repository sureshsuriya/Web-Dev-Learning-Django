# Generated by Django 4.2.3 on 2023-08-04 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0002_newdb_g'),
    ]

    operations = [
        migrations.AddField(
            model_name='newdb',
            name='cou',
            field=models.CharField(default=None, max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newdb',
            name='num',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]