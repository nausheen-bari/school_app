# Generated by Django 3.0.6 on 2020-06-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0009_auto_20200602_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
