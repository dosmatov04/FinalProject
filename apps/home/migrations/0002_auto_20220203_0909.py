# Generated by Django 3.2.7 on 2022-02-03 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='phone',
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100)),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_number', to='home.setting')),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номера',
            },
        ),
    ]