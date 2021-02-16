from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    description = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey(
        "auth.User", related_name="owner", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["id"]
