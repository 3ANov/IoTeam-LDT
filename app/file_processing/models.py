from django.db import models
from django.utils import timezone


class FileModel(models.Model):
    class ContentType(models.TextChoices):
        ODH_DATA = 'ODH_DATA'
        XlS_DATA = 'XlS_DATA'

    created_date = models.DateTimeField(default=timezone.now, verbose_name="время создания")
    content = models.FileField()
    content_type = models.CharField(max_length=8, choices=ContentType.choices, default=ContentType.XlS_DATA)