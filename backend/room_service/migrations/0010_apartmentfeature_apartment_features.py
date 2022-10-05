# Generated by Django 4.1.1 on 2022-10-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_service', '0009_apartment_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='features',
            field=models.ManyToManyField(blank=True, to='room_service.apartmentfeature'),
        ),
    ]
