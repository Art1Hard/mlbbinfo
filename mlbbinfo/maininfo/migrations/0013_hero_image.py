# Generated by Django 4.2.1 on 2024-12-31 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maininfo', '0012_alter_line_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
