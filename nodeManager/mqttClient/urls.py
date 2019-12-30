from django.urls import path
from . import views

urlpatterns = [
    path('connect/', views.connect),
    path('publish/', views.publish),
    path('subcribe/', views.subcribe),
    path('update/', views.update)
]
