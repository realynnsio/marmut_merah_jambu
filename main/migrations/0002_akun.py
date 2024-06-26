# Generated by Django 4.2.11 on 2024-05-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Akun',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('nama', models.CharField(max_length=100)),
                ('gender', models.IntegerField(choices=[(0, 'Female'), (1, 'Male')])),
                ('tempat_lahir', models.CharField(max_length=50)),
                ('tanggal_lahir', models.DateField()),
                ('is_verified', models.BooleanField()),
                ('kota_asal', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'marmut_akun',
            },
        ),
    ]
