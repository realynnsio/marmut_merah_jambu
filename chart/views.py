from django.shortcuts import render

def show_chart(request):
    context = {}
    return render(request, "list_chart.html", context)

def show_chart_detail(request):
    context = {}
    return render(request, "detail_chart.html", context)
