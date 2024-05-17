# Generated by Django 4.2.11 on 2024-05-17 07:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_genre_id_konten_alter_transaction_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songwriter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email_akun', models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.CASCADE, to='main.akun')),
                ('id_pemilik_hak_cipta', models.OneToOneField(db_column='id_pemilik_hak_cipta', on_delete=django.db.models.deletion.CASCADE, to='main.pemilikhakcipta')),
            ],
            options={
                'db_table': 'songwriter',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('kontak', models.CharField(max_length=50)),
                ('id_pemilik_hak_cipta', models.OneToOneField(db_column='id_pemilik_hak_cipta', on_delete=django.db.models.deletion.CASCADE, to='main.pemilikhakcipta')),
            ],
            options={
                'db_table': 'label',
            },
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('tipe', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('id_playlist', models.OneToOneField(db_column='id_playlist', on_delete=django.db.models.deletion.CASCADE, to='main.playlist')),
            ],
            options={
                'db_table': 'chart',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email_akun', models.OneToOneField(db_column='email_akun', on_delete=django.db.models.deletion.CASCADE, to='main.akun')),
                ('id_pemilik_hak_cipta', models.OneToOneField(db_column='id_pemilik_hak_cipta', on_delete=django.db.models.deletion.CASCADE, to='main.pemilikhakcipta')),
            ],
            options={
                'db_table': 'artist',
            },
        ),
        migrations.CreateModel(
            name='UserPlaylist',
            fields=[
                ('id_user_playlist', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('judul', models.CharField(max_length=100)),
                ('deskripsi', models.CharField(max_length=500)),
                ('jumlah_lagu', models.IntegerField()),
                ('tanggal_dibuat', models.DateField()),
                ('total_durasi', models.IntegerField(default=0)),
                ('email_pembuat', models.OneToOneField(db_column='email_pembuat', on_delete=django.db.models.deletion.CASCADE, to='main.akun')),
                ('id_playlist', models.OneToOneField(db_column='id_playlist', on_delete=django.db.models.deletion.CASCADE, to='main.playlist')),
            ],
            options={
                'db_table': 'user_playlist',
                'unique_together': {('email_pembuat', 'id_user_playlist')},
            },
        ),
    ]