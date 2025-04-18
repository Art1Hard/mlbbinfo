# Generated by Django 4.2.1 on 2025-01-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maininfo', '0016_introslide_alter_hero_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introslide',
            name='image',
            field=models.ImageField(upload_to='images/intro-slider/'),
        ),
        migrations.AlterField(
            model_name='line',
            name='icon',
            field=models.ImageField(upload_to='images/icons/lines'),
        ),
    ]
