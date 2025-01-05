from django.urls import path
from .views import process_get, user_form, upload_form

app_name = 'request_app'

urlpatterns = [
    path('get/', process_get, name='get-view'),
    path('info/', user_form, name='user_info'),
    path('file-upload/',  upload_form, name='file-upload'),

]