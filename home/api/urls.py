from django.urls import path
from home.api.views import (
    slider_list_api
)

urlpatterns = [
    path("slider-list/", slider_list_api, name="slider-list")
]
