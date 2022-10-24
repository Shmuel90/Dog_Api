# Generated by Django 4.1.2 on 2022-10-24 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_api', '0013_alter_breed_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Tiny', 'Tiny')], default='', max_length=6),
        ),
    ]
