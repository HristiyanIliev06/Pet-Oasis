# Generated by Django 5.0.6 on 2024-11-30 12:08

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat')], max_length=20)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('weight', models.FloatField(validators=[django.core.validators.MinValueValidator(0, message="It's not possible for your pet to weigh less than 0 kg!")])),
                ('image', models.ImageField(upload_to='profile_pics/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='accounts.profile')),
            ],
        ),
    ]
