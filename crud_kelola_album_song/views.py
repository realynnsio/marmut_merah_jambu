from django.shortcuts import render

# Create your views here.
def show_list_album(request):
    context = {
    }
    return render(request, "list_album.html", context)