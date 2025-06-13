from django.urls import path
from . import views

app_name = 'settings'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),  # якщо така буде
    path('albums/', views.albums_view, name='albums'),
    path('albums/create/', views.create_album, name='create_album'),
    path('albums/edit/<int:album_id>/', views.edit_album, name='edit_album'),
    path('albums/upload/', views.upload_photo, name='upload_photo'),
]