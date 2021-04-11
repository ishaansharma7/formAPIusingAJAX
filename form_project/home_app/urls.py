from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.user_list, name='list'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
