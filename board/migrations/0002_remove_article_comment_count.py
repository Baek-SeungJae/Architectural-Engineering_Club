# Generated by Django 3.0.7 on 2020-10-05 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comment_count',
        ),
    ]
