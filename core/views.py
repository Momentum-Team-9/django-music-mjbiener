# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Track


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'core/albums.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'core/album_details.html', {'album': album})


def add_album(request):
    # BASIC VIEW FUNCTION TO MAKE SURE URLS/HTML WORKING
    # NEED TO ADD NEW ALBUM FORM TO FORMS AND UPDATE VIEW
    return render(request, "core/new_album.html")


def edit_album(request, pk):
    # BASIC VIEW FUNCTION TO MAKE SURE URLS/HTML WORKING
    # NEED TO ADD EDIT ALBUM FORM TO FORMS AND UPDATE VIEW
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'core/edit_album.html', {'album': album})


def delete_album(request):
    pass
