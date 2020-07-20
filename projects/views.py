from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project
from django.utils import timezone

@login_required
def homepage(request):
    #return render(request, 'projects/index1.html')
    projects = Project.objects.all()
    #mediaUrl = 'http://'+request.get_host()+'/media' 
#    return render(request, 'projects/index1.html', {'projects': projects,'mediaurl':mediaUrl})
    return render(request, 'projects/index.html', {'projects': projects})

def home(request):
    return render(request, 'projects/loginRegister.html')

@login_required
def projectabout(request, project_pk):
    project = Project.objects.get(id=project_pk)
    return render(request, 'projects/project.html', {'project': project})
#    return render(request, 'project.html')

def registerForm(request):
    if request.method == 'GET':
        return render(request, 'projects/registerForm.html', {'form' :UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('homepage')
            except IntegrityError:
                return render(request, 'projects/registerForm.html', {'form': UserCreationForm(), "errMsg": "User name is already exist. Please choose a different one"})
        else:
            return render(request, 'projects/registerForm.html', {'form': UserCreationForm(), "errMsg": "Password did not match"})

@login_required
def myprojects(request):
    #projects = Project.objects.all()
    projects = Project.objects.filter(user_id=request.user).order_by('-dateCreated')
    return render(request, 'projects/myprojects.html', {'allprojects': projects})


@login_required
def allfaculties(request):
    return render(request, 'projects/faculties-list.html')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('projects-home')



def loginuser(request):
    if request.method == 'GET':
        return render(request, 'projects/loginform.html', {'form' :AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'projects/loginform.html', {'form': AuthenticationForm(), "errMsg": "User doesn't exist" })
        else:
            login(request, user)
            return redirect('homepage')

@login_required
def createNewProject(request):
    if request.method == 'GET':
        return render(request, 'projects/createnewproject.html', {'form':ProjectForm() })
    else:
        try:
            form = ProjectForm(request.POST, request.FILES)
            newProject = form.save(commit=False)
            newProject.user_id = request.user
            newProject.save()
            return redirect('my-projects')
        except ValueError:
            print(ValueError)
            return render(request, 'projects/createnewproject.html', {'form': ProjectForm(), 'errMsg': 'Data mismatch'})

@login_required
def allProjects(request):
    users = User.objects.all()
    projects = Project.objects.order_by('-dateCreated')
    return render(request, 'projects/allprojects.html', {'allprojects': projects, 'users': users})

@login_required
def updateproject(request, project_pk):
   project = get_object_or_404(Project, pk=project_pk, user_id=request.user)
   if (request.method == 'GET'):
       form = ProjectForm(instance=project)
       return render(request, 'projects/updateproject.html',{'project':project, 'form':form})
   else:
       try:
           form = ProjectForm(request.POST, instance=project)
           form.save()
           return redirect('my-projects')
       except ValueError:
           return render (request, 'projects/updateproject.html', {'form':form, 'errMsg': "Data mismatch"})

@login_required
def deleteproject(request, project_pk):
   project = get_object_or_404(Project, pk=project_pk, user_id=request.user)
   if (request.method == 'POST'):
       project.delete()
       return redirect('my-projects')

@login_required
def doneproject(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk, user_id=request.user)
    if request.method == 'POST':
        project.dateCompleted = timezone.now()
        project.save()
        return redirect('my-projects')


#@login_required
#def filterByProjectName(request):
#    users = User.objects.all()
#    projects = Project.objects.order_by('projectName')
#    return render(request, 'projects/allprojects.html', {'allprojects': projects, 'users': users})