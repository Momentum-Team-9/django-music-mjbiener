# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Track
from .forms import AlbumForm


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'core/albums.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'core/album_details.html', {'album': album})


def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='albums')
    return render(request, "core/new_album.html", {'form': form})


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method =='GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='albums')
    return render(request, 'core/edit_album.html', {'form': form, 'album': album})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='albums')
    
    return render(request, "core/delete_album.html", {"album": album})
