from django.urls import path

from .api import BookAPIView


urlpatterns =[
    path('', BookAPIView.as_view()),
]