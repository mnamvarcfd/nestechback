from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import FileResponse

from .models import TeamMembers
from .serializers import BackgroundVideoSerializer, TeamMembersSerializer
from .models import Services
from .models import BackgroundVideo
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
    

@api_view(['GET'])
def get_all_video(request):
    video = BackgroundVideo.objects.all()
    serilazer = BackgroundVideoSerializer(video, many=True)
    return Response(serilazer.data)
    
@api_view(['GET'])
def get_video(request, _id):
    try:
        video = get_object_or_404(BackgroundVideo, _id=_id)
    except BackgroundVideo.DoesNotExist:
        return Response({"error": "Video not found"}, status=404)

    video_file = video.video.path  # Assuming the video field is a FileField
    print("{video_file}")
    response = FileResponse(open(video_file, 'rb'))
    return response
