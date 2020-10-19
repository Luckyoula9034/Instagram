from django.urls import path,include
from .views import (
    PostListviews
)

app_name = 'insta'

urlpatterns = [
    path('',PostListviews.as_views(), name='post_list'),
]