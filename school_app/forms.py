from django.forms import ModelForm
from .models import *


class UpdateStudent(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class CreateStudent(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
