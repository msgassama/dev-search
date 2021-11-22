from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm


def projects(request):
    context={}

    projects = Project.objects.all().order_by('-created')

    context['projects']= projects
    return render(request, "projects/projects.html", context=context)

def project(request, pk):
    projectObj = Project.objects.get(pk=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project': projectObj, 'tags': tags})

def createProject(request):
    context = {}
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context['form'] = form

    return render(request, 'projects/project_form.html', context)

def updateProject(request, pk):
    project = Project.objects.get(pk=pk)
    context = {}
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context['form'] = form

    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    context = {}
    project = Project.objects.get(pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context['object'] = project

    return render(request, 'projects/delete_template.html', context)
