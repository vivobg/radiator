from .models import Application, ApplicationVersion, DeploymentEnvironment, Deployment
from rest_framework import viewsets
from .serializers import ApplicationSerializer, ApplicationVersionSerializer, DeploymentEnvironmentSerializer, DeploymentSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows applications to be viewed or edited.
    """
    queryset = Application.objects.all().order_by('-name')
    serializer_class = ApplicationSerializer

class ApplicationVersionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows applications to be viewed or edited.
    """
    queryset = ApplicationVersion.objects.all()
    serializer_class = ApplicationVersionSerializer


class DeploymentEnvironmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows environments to be viewed or edited.
    """
    queryset = DeploymentEnvironment.objects.all().order_by('-name')
    serializer_class = DeploymentEnvironmentSerializer

class DeploymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows deployments to be viewed or edited.
    """
    queryset = Deployment.objects.all().order_by('-deployment_start')
    serializer_class = DeploymentSerializer
