from django.contrib import admin
from .models import Paket, Akun, Konten, PemilikHakCipta, Premium, Playlist
from .models import NonPremium, Podcaster

# Register your models here.
admin.site.register(Akun)
admin.site.register(Konten)

admin.site.register(Paket)
admin.site.register(Playlist)
admin.site.register(PemilikHakCipta)

admin.site.register(Premium)
admin.site.register(NonPremium)
admin.site.register(Podcaster)
