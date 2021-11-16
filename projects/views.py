from django.shortcuts import render
from django.http import HttpResponse

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


    context['message'] = "Hello, you are on the projects page"
    context['number'] =10
    context['projects']=projectsList
    return render(request, "projects/projects.html", context=context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == int(pk):
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
