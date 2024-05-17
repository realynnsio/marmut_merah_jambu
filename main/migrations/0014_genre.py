# Generated by Django 4.2.11 on 2024-05-17 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_podcaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
                ('id_konten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.konten')),
            ],
            options={
                'db_table': 'genre',
                'unique_together': {('id_konten', 'genre')},
            },
        ),
    ]