from django.contrib.auth.models import User
from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Log(TimeStampedModel):
    user = models.IntegerField()
    app = models.CharField(null=True, max_length=255)
    status = models.CharField(null=True, max_length=255)
    request = models.JSONField(null=True)
    response = models.JSONField(null=True)

    class Meta:
        ordering = ("-created",)
        app_label = 'analytics'
