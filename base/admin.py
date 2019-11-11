from django.contrib import admin

# Register your models here.

from .models import Application, ApplicationVersion, DeploymentEnvironment, Deployment

admin.site.register(Application)
admin.site.register(ApplicationVersion)
admin.site.register(DeploymentEnvironment)
admin.site.register(Deployment)
