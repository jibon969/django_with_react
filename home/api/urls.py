from django.urls import path
from home.api.views import (
    slider_list_api,
    post_list,
    post_details
)

urlpatterns = [
    path("slider-list/", slider_list_api, name="slider-list"),
    path("post-list/", post_list, name="post-list"),
    path("post-detail/<slug:slug>/", post_details, name="post-detail")
]
