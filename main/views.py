from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {}
    return render(request, "main.html", context)

def show_login(request):
    context = {}
    return render(request, "login.html", context)