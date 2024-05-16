from django.shortcuts import render

# Create your views here.
def show_list_album(request):
    context = {}
    return render(request, "list_album.html", context)

def show_song_list_album(request):
    context = {}
    return render(request, "daftar_lagu.html", context)

def create_song(request):
    context = {}
    return render(request, "create_lagu.html", context)

def create_album(request):
    context = {}
    return render(request, "create_album.html", context)

def show_label_album(request):
    context = {}
    return render(request, "label_list_album.html", context)

def show_label_song_list(request):
    context = {}
    return render(request, "label_daftar_lagu.html", context)