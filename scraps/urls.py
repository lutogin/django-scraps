from scraps import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.get_info, name='info'),
]
