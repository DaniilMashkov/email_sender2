# Generated by Django 4.1.6 on 2023-02-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='views',
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Allow publish'),
        ),
    ]
