from django.db import models

# Create your models here.


class AboutMe(models.Model):
    name = models.CharField(max_length=120)
    position = models.CharField(max_length=120)
    about_me = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name
