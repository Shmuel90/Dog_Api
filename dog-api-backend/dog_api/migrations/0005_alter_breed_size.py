# Generated by Django 4.1.2 on 2022-10-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_api', '0004_alter_breed_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='size',
            field=models.CharField(choices=[('Medium', 'Medium'), ('Large', 'Large'), ('Small', 'Small'), ('Tiny', 'Tiny')], default='', max_length=6),
        ),
    ]
