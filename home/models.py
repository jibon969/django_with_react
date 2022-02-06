from django.db import models
from django.template.defaultfilters import truncatechars  # or truncatewords
from django_with_react.utils import unique_slug_generator
# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, help_text='slider title is mandatory')
    extraLargeDevices = models.ImageField(upload_to='slider/', null=True, blank=True, help_text="1920x597")
    largeDevices = models.ImageField(upload_to='slider/', null=True, blank=True, help_text="1400x400")
    mediumDevices = models.ImageField(upload_to='slider/', null=True, blank=True, help_text="800X400")
    smallDevices = models.ImageField(upload_to='slider/', null=True, blank=True, help_text="600x400")
    url_field = models.URLField(max_length=120, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True, verbose_name="Slider Position")
    active = models.BooleanField(default=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.FileField()
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

    def get_category_name(self):
        return self.category.title

    @property
    def short_description(self):
        return truncatechars(self.description, 30)


