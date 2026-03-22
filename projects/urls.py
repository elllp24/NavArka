from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "NavArka Admin"
admin.site.site_title = "NavArka Admin Portal"
admin.site.index_title = "Welcome to NavArka Dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    path('', views.home),
    path('projects/', views.project_list),
    path('projects/<int:pk>/', views.project_detail),
path('contact/', views.contact),
]

path('dashboard/', views.dashboard, name='dashboard'),
path('delete/<int:id>/', views.delete_project),

path('contact/', views.contact, name='contact'),

