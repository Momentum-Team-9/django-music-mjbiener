# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Track



def album_list(request):
    albums = Album.objects.all()
    return render(request, 'core/albums.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'core/album_detail.html', {'album': album})


def add_album(request):
    pass


def edit_album(request):
    pass


def delete_album(request):
    pass
