from django.urls import path
from . import views

urlpatterns = [
    path('json/', views.hello_world, name='hello_world'),
]
