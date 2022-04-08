from pyexpat import model
from tkinter import CASCADE
from django.db import models
from authapp.models import UserApp
from helpers.models import TrackingModel
from django.conf import settings

class Todo(TrackingModel):
    owner = models.ForeignKey(to=UserApp, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=settings.MEDIA_FOR_IMAGEFIELD)
    deadline = models.DateField(null=True, blank=True)
    # creationdate came from helpers.models.TrackingModel
    status = models.CharField(
        max_length=8,
        choices=(
            ("created", "created"),
            ("doing", "doing"),
            ("done","done")),
        default="created",
    )

    
    def __str__(self):
        return self.name
