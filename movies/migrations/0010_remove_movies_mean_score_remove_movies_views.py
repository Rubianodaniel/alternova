# Generated by Django 4.1.4 on 2022-12-22 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_rename_view_viewmovie_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='mean_score',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='views',
        ),
    ]