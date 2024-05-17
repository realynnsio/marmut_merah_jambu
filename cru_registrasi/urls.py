from django.urls import path

from cru_registrasi.views import show_registration_menu, registration_user_form, registration_label_form, register_user, login_form, login_user
from cru_registrasi.views import logout, register_label

app_name = 'cru_registrasi'

urlpatterns = [
    path('menu/', show_registration_menu, name='registration_menu'),
    path('user/', registration_user_form, name='registration_user_form'),
    path('label/', registration_label_form, name='registration_label_form'),
    path('registrasi/', register_user, name='registrasi_user'),
    path('registrasi-label/', register_label, name='registrasi_label'),
    path('login/', login_form, name='login_form'),
    path('login-validation/', login_user, name='login_user'),
    path('logout/', logout, name='logout'),
]