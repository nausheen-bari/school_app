# Generated by Django 3.0.6 on 2020-06-02 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0003_auto_20200602_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='picture',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
