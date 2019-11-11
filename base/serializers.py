from .models import Application, ApplicationVersion, DeploymentEnvironment, Deployment
from rest_framework import serializers


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ['name']

class ApplicationVersionSerializer(serializers.HyperlinkedModelSerializer):
    app = ApplicationSerializer(read_only=True)
    class Meta:
        model = ApplicationVersion
        fields = ['version', 'app']

class DeploymentEnvironmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeploymentEnvironment
        fields = ['name']

class DeploymentSerializer(serializers.HyperlinkedModelSerializer):

    app_version = ApplicationVersionSerializer(read_only=False)
    environment = DeploymentEnvironmentSerializer(read_only=True)

    class Meta:
        model = Deployment
        fields = [
        'app_version',
        'environment',
        'deployment_start',
        'deployment_status',
        ]
