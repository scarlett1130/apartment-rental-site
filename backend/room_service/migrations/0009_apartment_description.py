# Generated by Django 4.1.1 on 2022-10-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_service', '0008_apartmenttype_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='description',
            field=models.TextField(default=''),
        ),
    ]