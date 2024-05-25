from . import views
from django.urls import path

urlpatterns = [
    path('create-session/',views.session_create, name='session_create'),
    path('meditation/', views.meditation, name='meditation-begins'),
]