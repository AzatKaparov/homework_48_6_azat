# Generated by Django 2.2 on 2020-08-01 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200731_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.CharField(blank=True, max_length=1500, null=True, verbose_name='Ссылка на фотографию'),
        ),
    ]