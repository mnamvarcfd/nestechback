from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import FileResponse

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .serializers import ContactForm


from .models import TeamMembers
from .serializers import BackgroundVideoSerializer, TeamMembersSerializer
from .models import Services
from .models import Projects
from .models import BackgroundVideo
from .serializers import ServicesSerializer
from .serializers import ProjectsSerializer


def getRoutes(request):
    return JsonResponse("hi", safe=False)

@api_view(['GET'])
def get_team_members(request):
    members = TeamMembers.objects.all()
    serilazer = TeamMembersSerializer(members, many=True)
    return Response(serilazer.data)
    
# @api_view(['GET'])
# def get_team_member(request, pk):
#     member = TeamMembers.objects.get(_id=pk)
#     serilazer = TeamMembersSerializer(member, many=False)
#     return Response(serilazer.data)
    

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
def get_video(request):
    _id = request.GET.get('_id')
    
    if _id is None:
        return JsonResponse({"error": "_id parameter is required"}, status=400)

    try:
        video = get_object_or_404(BackgroundVideo, _id=_id)
    except BackgroundVideo.DoesNotExist:
        return JsonResponse({"error": "Video not found"}, status=404)

    video_file = video.video.path

    response = FileResponse(open(video_file, 'rb'))
    return response

@api_view(['GET'])
def get_team_member_imag(request):
    _id = request.GET.get('_id')
    
    if _id is None:
        return JsonResponse({"error": "_id parameter is required"}, status=400)

    try:
        team_member = get_object_or_404(TeamMembers, _id=_id)
    except TeamMembers.DoesNotExist:
        return JsonResponse({"error": "image not found"}, status=404)

    imag_file = team_member.image.path

    response = FileResponse(open(imag_file, 'rb'))
    return response


@api_view(['GET'])
def get_service_imag(request):
    _id = request.GET.get('_id')
    
    if _id is None:
        return JsonResponse({"error": "_id parameter is required"}, status=400)

    try:
        service = get_object_or_404(Services, _id=_id)
    except Services.DoesNotExist:
        return JsonResponse({"error": "image not found"}, status=404)

    imag_file = service.image.path

    response = FileResponse(open(imag_file, 'rb'))
    return response


@csrf_exempt
@require_POST
def contact_api(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        contact = form.save()

        # Send email to the app owner
        subject = f'New Contact: {contact.name}'
        message = f'Name: {contact.name}\nEmail: {contact.email}\nMessage: {contact.message}'
        from_email = 'your-email@example.com'
        to_email = 'app-owner-email@example.com'
        send_mail(subject, message, from_email, [to_email])

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors})
    
    
    
    

@api_view(['GET'])
def get_projects(request):
    projects = Projects.objects.all()
    serilazer = ProjectsSerializer(projects, many=True)
    return Response(serilazer.data)

@api_view(['GET'])
def get_project_imag(request):
    _id = request.GET.get('_id')
    
    if _id is None:
        return JsonResponse({"error": "_id parameter is required"}, status=400)

    try:
        service = get_object_or_404(Services, _id=_id)
    except Projects.DoesNotExist:
        return JsonResponse({"error": "image not found"}, status=404)

    imag_file = service.image.path

    response = FileResponse(open(imag_file, 'rb'))
    return response

