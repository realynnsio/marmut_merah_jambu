from django.db import models
import uuid

class Paket(models.Model):
    jenis = models.CharField(max_length=50, primary_key=True)
    harga = models.IntegerField()

    class Meta:
        db_table = 'paket'  # Specify the exact table name in the database

class Akun(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    GENDER_CHOICES = (
        (0, 'Female'),
        (1, 'Male'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES)
    tempat_lahir = models.CharField(max_length=50)
    tanggal_lahir = models.DateField()
    is_verified = models.BooleanField()
    kota_asal = models.CharField(max_length=50)
    
    # Add any additional fields or methods as needed

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'akun'  # Specify the exact table name in the database

    def check_password(self, raw_password):
        """
        Check if the given raw password matches the stored password for this user.
        """
        return raw_password == self.password

class Konten(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    judul = models.CharField(max_length=100)
    tanggal_rilis = models.DateField()
    tahun = models.IntegerField()
    durasi = models.IntegerField()

    class Meta:
        db_table = 'konten'  # Specify the exact table name in the database

class PemilikHakCipta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rate_royalti = models.IntegerField()

    class Meta:
        db_table = 'pemilik_hak_cipta'