# Generated by Django 3.1 on 2020-11-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201103_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade2blogpost',
            name='file',
            field=models.FileField(upload_to='blog/downloads/'),
        ),
        migrations.AlterField(
            model_name='grade3blogpost',
            name='file',
            field=models.FileField(upload_to='blog/downloads/'),
        ),
        migrations.AlterField(
            model_name='grade4blogpost',
            name='file',
            field=models.FileField(upload_to='blog/downloads/'),
        ),
    ]
