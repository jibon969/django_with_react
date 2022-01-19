from django.contrib import admin
from .models import Slider, Post

# Register Slider models is here.


class SliderAdmin(admin.ModelAdmin):
    class Meta:
        model = Slider
        list_display = ['title', 'value', 'url_field', 'active']
        list_editable = ['value', 'active']


admin.site.register(Slider, SliderAdmin)


class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
        list_display = ['title']


admin.site.register(Post, PostAdmin)
