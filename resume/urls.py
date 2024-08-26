from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('api_project/', views.api_project, name='api_project'),
    path('crm/', views.crm, name='crm'),
    path('restaurant/', views.restaurant, name='restaurant'),
]