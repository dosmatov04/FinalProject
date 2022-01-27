from django.db import models

# Create your models here.
class Price(models.Model):
    title = models.name = models.CharField(
        max_length=255, verbose_name="Название",
        help_text="Например: Супервыгодный"
    )
    description = models.TextField(verbose_name="Описание")
    price = models.CharField(
        max_length=100, verbose_name="Цена",
        help_text="Например: 100$ / за месяц"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Цена"