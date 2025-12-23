from django.urls import path

from . views import *


app_name = 'api'

urlpatterns = [
    path('check-user-status', CheckUserStatusAPIView.as_view()),
]
