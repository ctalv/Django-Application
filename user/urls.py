# map urls to views functions

from django.urls import path, include
from . import views

# URLConf
urlpatterns = [
    # path('users/', views.home, name='home'),
    path('', views.post, name='post'),
    path('<int:user_id>/', views.edit, name='edit_user'),
]