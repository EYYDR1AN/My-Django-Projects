# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.department_list, name='department_list'),
#     path('add/', views.department_create, name='department_create'),
#     path('edit/<int:id>/', views.department_edit, name='department_edit'),
#     path('delete/<int:id>/', views.department_delete, name='department_delete'),
# ]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('games.urls')),
]