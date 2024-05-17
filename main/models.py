from django.db import models

class Paket(models.Model):
    jenis = models.CharField(max_length=50, primary_key=True)
    harga = models.IntegerField()

    class Meta:
        db_table = 'paket'  # Specify the exact table name in the database
