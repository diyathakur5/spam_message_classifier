from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Link the index view to the root URL
]
