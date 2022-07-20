from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

#--------------------------------------------------------------------------------------------
#List Project
def projects(request):
    project = Project.objects.all()
    context ={'project':project}
    return render(request,'projects/projects.html', context)

#----------------------------------------------------------------------------------------------
#details project
def project(request, pk):
    projectObj= Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    context ={'project':projectObj, 'tags':tags}
    return render(request,'projects/single-project.html',context)
#----------------------------------------------------------------------------------------------
#creat project

def createProject(request):
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    
    context ={'form':form}
    return render(request, 'projects/project_form.html', context)

#----------------------------------------------------------------------------------------------
#update project

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance = project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    
    context ={'form':form}
    return render(request, 'projects/project_form.html', context)

#----------------------------------------------------------------------------------------------
#update project

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request,'projects/delete_template.html', context)