from django.urls import path

from .views import hello_world, GroupListAPIView

app_name = 'test_api'

urlpatterns = [
    path('hello/', hello_world, name='hello'),
    path('groups/', GroupListAPIView.as_view(), name='groups'),


]