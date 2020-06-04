# Generated by Django 3.0.6 on 2020-06-02 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0011_student_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='Ab', max_length=1, null=True),
        ),
    ]
