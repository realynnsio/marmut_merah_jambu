from django.shortcuts import render

def show_list_podcast(request):
    context = {}
    return render(request, "list_podcast.html", context)

def show_list_episode(request):
    context = {}
    return render(request, 'list_episode.html', context)

def show_podcast_detail(request):
    context = {}
    return render(request, "podcast_detail.html", context)

def show_form(request):
    context = {}
    return render(request, "create_episode.html", context)