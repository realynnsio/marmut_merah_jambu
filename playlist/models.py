from django.db import models
import uuid

# Create your models here.

class Playlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        db_table = 'playlist'  # Specify the exact table name in the database