from django.shortcuts import render

# Create your views here.
def show_dashboard(request):
    context = {}
    return render(request, "dashboard.html", context)
