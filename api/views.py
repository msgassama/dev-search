from django.http import HttpRequest
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request as restRequest
from .serializers import ProjectSerializer
from projects.models import Project, Review
from typing import Union


@api_view(['GET'])
def getRoutes(request: HttpRequest):
    
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},
        
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    
    return Response(routes)

@api_view(['GET'])
def getProjects(request: HttpRequest):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True, context={"request":request})
    
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request: HttpRequest, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, context={"request":request})
    
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request: Union[HttpRequest, restRequest], pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    
    review, created = Review.objects.get_or_create(
        owner=user,
        project=project
    )
    
    review.value = data['value']
    review.save()
    project.getVoteCount
    
    print(f"DATA: {data}")
    
    serializer = ProjectSerializer(project)
    
    return Response(serializer.data)