from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['fullName','email','phone','projectName','keyWord', 'description', 'fasion','art' ,'chemical','jewellery' ,'graphic', 'electronic', 'software' , 'industrial', 'Textil']

    