from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = "NavArka Admin"
admin.site.site_title = "NavArka Admin Portal"
admin.site.index_title = "Welcome to NavArka Dashboard"

urlpatterns = [
    # ✅ Admin
    path('admin/', admin.site.urls),

    # ✅ Website pages
    path('', views.home),
    path('projects/', views.project_list),
    path('projects/<int:pk>/', views.project_detail),
    path('contact/', views.contact, name='contact'),

    # ✅ Extra features
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete/<int:id>/', views.delete_project),
]
