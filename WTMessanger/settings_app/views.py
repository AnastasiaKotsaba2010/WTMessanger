from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

def albums_view(request):
    albums = Album.objects.all()
    return render(request, 'settings_app/albums.html', {'albums': albums})

def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('settings:albums')

def edit_album(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('settings:albums')
    return render(request, 'settings_app/edit_album.html', {'album': album})

def upload_photo(request):
    # тут логіка завантаження фото
    pass

def profile_view(request):
    return render(request, 'settings_app/profile.html')