from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BackgroundVideo
from .models import TeamMembers
from .models import Services

class TeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = '__all__'
        
class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
        
class BackgroundVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundVideo
        fields = '__all__'