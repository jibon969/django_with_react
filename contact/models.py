from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.email
