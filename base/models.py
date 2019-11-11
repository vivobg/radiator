from django.db import models

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return self.name

class ApplicationVersion(models.Model):
    app = models.ForeignKey(Application, on_delete=models.CASCADE)
    version = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.app.name}: {self.version}"

class DeploymentEnvironment(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.name}"

class Deployment(models.Model):
    app_version = models.ForeignKey(ApplicationVersion, on_delete=models.CASCADE)
    environment = models.ForeignKey(DeploymentEnvironment, on_delete=models.CASCADE)
    deployment_start = models.DateTimeField()
    deployment_status = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.deployment_start} {self.deployment_status} {self.app_version.app.name} {self.app_version.version} {self.environment}"
