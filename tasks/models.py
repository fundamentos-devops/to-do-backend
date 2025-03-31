from django.db import models
from tasks.choices import Status


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
     
    def __str__(self):
        return self.title
