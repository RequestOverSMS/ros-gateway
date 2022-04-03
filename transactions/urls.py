from django.urls import path
from . import views


urlpatterns = [
    path(r'ros', views.ROSView.as_view(), name='ros'),
]

