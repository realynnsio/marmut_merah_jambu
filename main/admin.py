from django.contrib import admin
from .models import Paket, Akun, Konten, PemilikHakCipta

# Register your models here.
admin.site.register(Paket)
admin.site.register(Akun)
admin.site.register(Konten)
admin.site.register(PemilikHakCipta)
