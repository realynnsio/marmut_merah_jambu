from django.shortcuts import render


def show_main(request):
    context = {}
    return render(request, "main.html", context)

def show_login(request):
    context = {}
    return render(request, "login.html", context)
