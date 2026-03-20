from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('projects/', views.project_list),
    path('projects/<int:pk>/', views.project_detail),
path('contact/', views.contact),
]

path('dashboard/', views.dashboard, name='dashboard'),
path('delete/<int:id>/', views.delete_project),

path('contact/', views.contact, name='contact'),