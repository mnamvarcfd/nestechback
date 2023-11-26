from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import TeamMembers
from .serializers import TeamMembersSerializer
from .models import Services
from .serializers import ServicesSerializer


def getRoutes(request):
    return JsonResponse("hi", safe=False)

@api_view(['GET'])
def get_team_members(request):
    members = TeamMembers.objects.all()
    serilazer = TeamMembersSerializer(members, many=True)
    return Response(serilazer.data)
    
@api_view(['GET'])
def get_team_member(request, pk):
    member = TeamMembers.objects.get(_id=pk)
    serilazer = TeamMembersSerializer(member, many=False)
  
    return Response(serilazer.data)
    

@api_view(['GET'])
def get_services(request):
    services = Services.objects.all()
    serilazer = ServicesSerializer(services, many=True)
    return Response(serilazer.data)
    