# Generated by Django 3.0.6 on 2020-06-02 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0005_auto_20200602_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(blank=True, default='index.png', null=True, upload_to=''),
        ),
    ]
