from django.urls import path
from cru_registrasi.views import show_registration_menu, registration_user_form, registration_label_form

app_name = 'cru_registrasi'

urlpatterns = [
    path('menu/', show_registration_menu, name='registration_menu'),
    path('user/', registration_user_form, name='registration_user_form'),
    path('label/', registration_label_form, name='registration_label_form'),
]