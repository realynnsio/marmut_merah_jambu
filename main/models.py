from django.db import models
import uuid

# AKUN ----------------------------------------------------------------------------------------
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

# KONTEN ----------------------------------------------------------------------------------------

class Konten(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    judul = models.CharField(max_length=100)
    tanggal_rilis = models.DateField()
    tahun = models.IntegerField()
    durasi = models.IntegerField()

    class Meta:
        db_table = 'konten'  # Specify the exact table name in the database

# PAKET ----------------------------------------------------------------------------------------

class Paket(models.Model):
    jenis = models.CharField(max_length=50, primary_key=True)
    harga = models.IntegerField()

    class Meta:
        db_table = 'paket'  # Specify the exact table name in the database

# PLAYLIST ----------------------------------------------------------------------------------------

class Playlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        db_table = 'playlist'  # Specify the exact table name in the database

# PEMILIK HAK CIPTA --------------------------------------------------------------------------------

class PemilikHakCipta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rate_royalti = models.IntegerField()

    class Meta:
        db_table = 'pemilik_hak_cipta'

# PREMIUM ----------------------------------------------------------------------------------------

class Premium(models.Model):
    email = models.OneToOneField(Akun, on_delete=models.CASCADE, primary_key=True, db_column='email')

    class Meta:
        db_table = 'premium'

# NON PREMIUM ----------------------------------------------------------------------------------------

class NonPremium(models.Model):
    email = models.OneToOneField(Akun, on_delete=models.CASCADE, primary_key=True, db_column='email')

    class Meta:
        db_table = 'non_premium'

# PODCASTER ----------------------------------------------------------------------------------------

class Podcaster(models.Model):
    email = models.OneToOneField(Akun, on_delete=models.CASCADE, primary_key=True, db_column='email')

    class Meta:
        db_table = 'podcaster'

# GENRE ----------------------------------------------------------------------------------------

class Genre(models.Model):
    id_konten = models.OneToOneField(Konten, on_delete=models.CASCADE, primary_key=True, to_field='id', db_column='id_konten')
    genre = models.CharField(max_length=50)

    class Meta:
        db_table = 'genre'
        unique_together = ('id_konten', 'genre')

# TRANSACTION ----------------------------------------------------------------------------------------

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jenis_paket = models.OneToOneField(Paket, on_delete=models.CASCADE, to_field='jenis', db_column='jenis_paket')
    email = models.OneToOneField(Akun, on_delete=models.CASCADE, to_field='email', db_column='email')
    timestamp_dimulai = models.DateTimeField()
    timestamp_berakhir = models.DateTimeField()
    metode_bayar = models.CharField(max_length=50)
    nominal = models.IntegerField()

    class Meta:
        db_table = 'transaction'
        unique_together = ('id', 'jenis_paket', 'email')

    def __str__(self):
        return f"Transaction {self.id} for {self.email}"

# SONGWRITER ----------------------------------------------------------------------------------------

class Songwriter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email_akun = models.OneToOneField(Akun, on_delete=models.CASCADE, to_field='email', db_column='email')
    id_pemilik_hak_cipta = models.OneToOneField(PemilikHakCipta, on_delete=models.CASCADE, to_field='id', db_column='id_pemilik_hak_cipta')

    class Meta:
        db_table = 'songwriter'

    def __str__(self):
        return f"Songwriter {self.id}"
    
# USER PLAYLIST ----------------------------------------------------------------------------------------

class UserPlaylist(models.Model):
    email_pembuat = models.OneToOneField(Akun, on_delete=models.CASCADE, to_field='email', db_column='email_pembuat')
    id_user_playlist = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    judul = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=500)
    jumlah_lagu = models.IntegerField()
    tanggal_dibuat = models.DateField()
    id_playlist = models.OneToOneField(Playlist, on_delete=models.CASCADE, to_field='id', db_column='id_playlist')
    total_durasi = models.IntegerField(default=0)

    class Meta:
        db_table = 'user_playlist'
        unique_together = ('email_pembuat', 'id_user_playlist')

    def __str__(self):
        return f"Playlist {self.judul} by {self.email_pembuat}"

# CHART ----------------------------------------------------------------------------------------

class Chart(models.Model):
    tipe = models.CharField(max_length=50, primary_key=True)
    id_playlist = models.OneToOneField(Playlist, on_delete=models.CASCADE, to_field='id', db_column='id_playlist')

    class Meta:
        db_table = 'chart'

    def __str__(self):
        return self.tipe
    
# LABEL ----------------------------------------------------------------------------------------

class Label(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    kontak = models.CharField(max_length=50)
    id_pemilik_hak_cipta = models.OneToOneField(PemilikHakCipta, on_delete=models.CASCADE, to_field='id', db_column='id_pemilik_hak_cipta')

    class Meta:
        db_table = 'label'

    def __str__(self):
        return self.nama

# ARTIST ----------------------------------------------------------------------------------------

class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email_akun = models.OneToOneField(Akun, on_delete=models.CASCADE, to_field='email', db_column='email_akun')
    id_pemilik_hak_cipta = models.OneToOneField(PemilikHakCipta, on_delete=models.CASCADE, to_field='id', db_column='id_pemilik_hak_cipta')

    class Meta:
        db_table = 'artist'

    def __str__(self):
        return f"Artist {self.id}"