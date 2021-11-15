
from django.contrib import admin
from django.urls import path

from segments import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/', views.create_user, name='create_user'),
    path('create_tag/', views.create_tag, name='create_tag'),
    path('create_segments/', views.create_segments, name='create_segments'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('delete_tag/', views.delete_tag, name='delete_tag'),
    path('delete_segments/', views.delete_segments, name='delete_segments'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('edit_tag/', views.edit_tag, name='edit_tag'),
    path('edit_segments/', views.edit_user_tag, name='edit_segments'),
    path('filter/', views.filter_user_tag, name='filter'),
    path('delete/', views.delete_user, name='delete'),
]
