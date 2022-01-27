from django.db import models

class Service(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название",
        help_text="Например Заголовок: Кирпич мне в голову"
    )
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="service",verbose_name="Название",
        help_text="Уютные Квартиры"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Услуги'
