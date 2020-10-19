from django.urls import path,include
from .views import (
    PostListview
)

app_name = 'insta'

urlpatterns = [
    path('',PostListview.as_view(), name='post_list'),
]