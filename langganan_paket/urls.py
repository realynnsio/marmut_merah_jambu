from django.urls import path
from langganan_paket.views import show_list_paket, show_pembayaran, show_riwayat1, submit_payment

app_name = 'langganan_paket'

urlpatterns = [
    path('show_list_paket/', show_list_paket, name='show_list_paket'),
    path('payment/', show_pembayaran, name= 'show_pembayaran'),
    path('payment/submit-payment/', submit_payment, name= 'submit_payment'),
    path('show_riwayat/', show_riwayat1, name= 'show_riwayat'),
]