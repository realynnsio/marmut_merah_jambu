# Generated by Django 4.2.11 on 2024-05-17 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_genre_id_konten_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='id_konten',
            field=models.OneToOneField(db_column='id_konten', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.konten'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='email',
            field=models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.CASCADE, to='main.akun'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='jenis_paket',
            field=models.OneToOneField(db_column='jenis_paket', on_delete=django.db.models.deletion.CASCADE, to='main.paket'),
        ),
    ]
