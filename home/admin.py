from django.contrib import admin
from .models import Slider, Post, Category

# Register Slider models is here.


class SliderAdmin(admin.ModelAdmin):
    class Meta:
        model = Slider
        list_display = ['title', 'value', 'url_field', 'active']
        list_editable = ['value', 'active']


admin.site.register(Slider, SliderAdmin)


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
        list_display = ['title']


admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

    class Meta:
        model = Post
        list_display = ['title', 'slug']


admin.site.register(Post, PostAdmin)
