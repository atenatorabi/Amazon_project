# Generated by Django 5.2 on 2025-06-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactUs_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactusmodel',
            options={'verbose_name': 'پیام', 'verbose_name_plural': 'پیام ها'},
        ),
        migrations.AddField(
            model_name='contactusmodel',
            name='is_read_by_admin',
            field=models.BooleanField(default=False, verbose_name='خوانده شده'),
        ),
    ]
