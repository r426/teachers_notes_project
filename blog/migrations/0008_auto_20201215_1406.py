# Generated by Django 3.1 on 2020-12-15 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201117_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade2blogpost',
            name='intro',
            field=models.TextField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grade3blogpost',
            name='intro',
            field=models.TextField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grade4blogpost',
            name='intro',
            field=models.TextField(default='intro', max_length=400),
        ),
        migrations.AlterField(
            model_name='grade2blogpost',
            name='title',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='grade3blogpost',
            name='title',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='grade4blogpost',
            name='title',
            field=models.TextField(max_length=200),
        ),
    ]
