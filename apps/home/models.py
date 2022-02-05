from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=150)
    logo = models.ImageField(blank=True,upload_to='images/')
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address = models.CharField(blank=True,max_length=100)
    working_hours = models.CharField(max_length=250)
    email = models.CharField(blank=True,max_length=50)
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    telegram = models.CharField(blank=True, max_length=50)
    backround_image = models.ImageField(upload_to = 'backround_image/')

    def __str__(self):
        return f"ID: {self.id} ||||| Title: {self.title}"
    
    class Meta:
        verbose_name_plural = "Настройки"

class Phone(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE, related_name='phone_number')
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.phone 

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"