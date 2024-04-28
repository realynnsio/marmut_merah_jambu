from django.shortcuts import render

# Create your views here.
def show_registration_menu(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "registration_menu.html", context)

def registration_user_form(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "registration_user_form.html", context)

def registration_label_form(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "registration_label_form.html", context)