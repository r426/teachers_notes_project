# Generated by Django 3.1 on 2020-12-15 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20201215_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade2blogpost',
            name='imagecredits',
            field=models.TextField(default='Image from pixabay.com', max_length=400),
        ),
        migrations.AlterField(
            model_name='grade3blogpost',
            name='imagecredits',
            field=models.TextField(default='Image from pixabay.com', max_length=400),
        ),
        migrations.AlterField(
            model_name='grade4blogpost',
            name='imagecredits',
            field=models.TextField(default='Image from pixabay.com', max_length=400),
        ),
    ]
