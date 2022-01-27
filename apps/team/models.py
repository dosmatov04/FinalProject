from django.db import models

# Create your models here.

class Team(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название",
        help_text="Например: Досматов Дилмурат"
    )
    position = models.CharField(
        max_length=255,verbose_name="Должность",
        help_text="Например: construction-engineer"
        )
    description = models.TextField(verbose_name="биография")
    image = models.ImageField(
        upload_to="team", verbose_name=""
    )