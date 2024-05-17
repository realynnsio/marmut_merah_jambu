from django.urls import path
from chart.views import show_chart, show_chart_detail

app_name = 'chart'

urlpatterns = [
    path('', show_chart, name='show_chart'),
    path('chart-details/', show_chart_detail, name='show_chart_detail'),
]