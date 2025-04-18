# Generated by Django 4.2.1 on 2025-01-22 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maininfo', '0015_line_icon_alter_hero_alt_alter_hero_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntroSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='images/intro-slider/')),
            ],
        ),
        migrations.AlterField(
            model_name='hero',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/heroes/'),
        ),
    ]
