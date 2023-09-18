# map urls to views functions

from django.urls import path, include
from . import views

# URLConf
urlpatterns = [
    # path('users/', views.home, name='home'),
    path('users/', views.post, name='post'),
    path('users/<int:user_id>/', views.edit, name='edit_user'),
]