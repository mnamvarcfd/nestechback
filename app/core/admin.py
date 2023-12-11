from django.contrib import admin
from .models import BackgroundVideo, TeamMembers
from .models import Services

admin.site.register(TeamMembers)
admin.site.register(Services)
admin.site.register(BackgroundVideo)
