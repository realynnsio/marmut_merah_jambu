from django.urls import path
from chart.views import show_chart, chart_detail_daily, chart_detail_year, chart_detail_monthly, chart_detail_weekly

app_name = 'chart'

urlpatterns = [
    path('', show_chart, name='show_chart'),
    path('chart-detail-daily/', chart_detail_daily, name='chart_detail_daily'),
    path('chart-detail-year/', chart_detail_year, name='chart_detail_year'),
    path('chart-detail-monthly/', chart_detail_monthly, name='chart_detail_monthly'),
    path('chart-detail-weekly/', chart_detail_weekly, name='chart_detail_weekly'),

]