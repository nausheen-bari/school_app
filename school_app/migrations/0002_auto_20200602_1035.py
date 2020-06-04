# Generated by Django 3.0.6 on 2020-06-02 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_app.Employee'),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='school_app.Course'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('Administration', 'Administration'), ('IT', 'IT'), ('Maintainance & Support', 'Maintainance & Support'), ('Academics', [('Maths', 'Maths'), ('Science', 'Science'), ('Social Studies', 'Social Studies'), ('Language', 'Language')])], max_length=200, null=True),
        ),
    ]
