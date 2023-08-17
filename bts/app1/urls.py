
from django.urls import path
from . import views
urlpatterns = [
    path('register', views.register, name='index2'),
    path('login', views.login, name='login'),
    path('index', views.index, name='seat')
]
