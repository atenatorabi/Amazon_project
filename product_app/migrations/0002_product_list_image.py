# Generated by Django 5.2 on 2025-06-02 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_list',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='اضافه کردن عکس محصول'),
        ),
    ]
