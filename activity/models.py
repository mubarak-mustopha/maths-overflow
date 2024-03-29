from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Action(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    # set up generic relation
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField()
    target = GenericForeignKey("target_content_type", "target_id")

    class Meta:
        ordering = ["-created"]
