from . import views
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    #path('settings/', views.settings, name='settings'),

]
