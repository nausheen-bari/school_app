import uuid
from django.db import models

# Create your models here.


class Employee(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    DEPT = [
        ('Administration', 'Administration'),
        ('IT', 'IT'),
        ('Maintainance & Support', 'Maintainance & Support'),
        ('Academics', [('Maths', 'Maths'), ('Science', 'Science'), ('Social Studies', 'Social Studies'), ('Language', 'Language')
                       ])
    ]

    f_name = models.CharField(max_length=200, null=True)
    l_name = models.CharField(max_length=200, null=True)
    m_name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, choices=GENDER)
    department = models.CharField(max_length=200, null=True, choices=DEPT)
    picture = models.ImageField(blank=True, null=True, default="index.png")

    #id = models.UUIDField(primary_key=True,max_length=6,default=uuid.uuid4,editable=False)

    def __str__(self):
        return self.l_name


class Course(models.Model):
    DEPT = [
        ('Math', 'Math'),
        ('Science', 'Science'), ('Social Studies', 'Social Studies'),
        ('Language', [('Hindi', 'Hindi'),
                      ('English', 'English'), ('Kannada', 'Kannada')]),

    ]
    LEVEL = [
        ('Primary', 'Primary (1-4)'),
        ('Middle', 'Middle (5-7)'),
        ('High School', 'High School(8-10)')
    ]
    fullname = models.CharField(max_length=200, null=True)
    shortname = models.CharField(max_length=5, null=True)
    period = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True, choices=DEPT)
    level = models.CharField(max_length=200, null=True, choices=LEVEL)
    teacher = models.ForeignKey(
        Employee, null=True, on_delete=models.SET_NULL, default=None)

    def __str__(self):
        return self.shortname


class Student(models.Model):
    LANG = [
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Kannada', 'Kannada')]
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    GRADES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    ]
    f_name = models.CharField(max_length=200, null=True)
    l_name = models.CharField(max_length=200, null=True)
    m_name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, choices=GENDER)
    #id = models.UUIDField(primary_key=True,max_length=6,default=uuid.uuid4,editable=False)
    grad_date = models.DateField()
    coy = models.DateField()
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)
    language = models.CharField(max_length=200, null=True, choices=LANG)
    dob = models.DateField()
    parent_details = models.TextField(max_length=200, null=True, blank=True)
    picture = models.ImageField(blank=True, null=True, default="index.png")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
    grade = models.CharField(max_length=1, null=True,
                             blank=True, default=None, choices=GRADES)

    def __str__(self):
        return self.l_name
