from django.conf import settings
from .models import Project

def project_list_ctx(request):
    project_list = Project.objects.order_by('project_rank')
    return({'project_list':project_list})

def media_url(request):
    return({'MEDIA_URL':settings.MEDIA_URL})

def static_url(request):
    return({'SETTINGS_STATIC_URL':settings.STATIC_URL})