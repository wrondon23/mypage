from django.shortcuts import render
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
    context ={'form':form}
    return render(request, 'projects/project_form.html', context)