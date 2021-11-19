from django.shortcuts import render
from .models import Project

# Create your views here.
projectsList = [
    {
        'id': 1,
        'title': "Elearning Website",
        'description': 'Fully functionnal e-learning website'
    },
    {
        'id': 2,
        'title': "Marketplace Website",
        'description': 'Fully functionnal marketplace website'
    },
    {
        'id': 3,
        'title': "Ecommerce Website",
        'description': 'Fully functionnal ecommerce website'
    },
]

def projects(request):
    context={}

    projects = Project.objects.all()

    context['projects']= projects
    return render(request, "projects/projects.html", context=context)

def project(request, pk):
    projectObj = Project.objects.get(pk=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project': projectObj, 'tags': tags})
