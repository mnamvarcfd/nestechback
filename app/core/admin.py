from django.contrib import admin
from .models import BackgroundVideo, Contact, TeamMembers, Projects
from .models import Services

admin.site.register(TeamMembers)
admin.site.register(Services)
admin.site.register(Projects)
admin.site.register(BackgroundVideo)
admin.site.register(Contact)
