# Generated by Django 3.2.7 on 2022-01-29 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('logo', models.ImageField(blank=True, upload_to='images/')),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('facebook', models.CharField(blank=True, max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('telegram', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
