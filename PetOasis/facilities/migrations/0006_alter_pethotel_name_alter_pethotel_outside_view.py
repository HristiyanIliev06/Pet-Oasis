# Generated by Django 5.0.6 on 2024-12-17 18:38

import core.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0005_alter_pethotel_outside_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pethotel',
            name='name',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(8, message="The pet hotel's name must consist of at least 8 letters!"), core.validators.pet_hotel_and_shelter_name_validator]),
        ),
        migrations.AlterField(
            model_name='pethotel',
            name='outside_view',
            field=models.URLField(blank=True, null=True),
        ),
    ]
