# Generated by Django 5.1.3 on 2024-12-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.ImageField(upload_to='profile_pics/pets/'),
        ),
    ]
