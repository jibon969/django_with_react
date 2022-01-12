from django.contrib import admin
from .models import Slider

# Register Slider models is here.


class SliderAdmin(admin.ModelAdmin):
    resource_class = Slider
    list_display = ['title', 'value', 'url_field', 'active']
    list_editable = ['value', 'active']


admin.site.register(Slider, SliderAdmin)
