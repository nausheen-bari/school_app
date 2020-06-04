# Generated by Django 3.0.6 on 2020-06-02 15:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0008_auto_20200602_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]