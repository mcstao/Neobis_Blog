# Generated by Django 4.2.6 on 2023-11-04 07:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 7, 6, 43, 1771, tzinfo=datetime.timezone.utc), verbose_name='Время публикации'),
        ),
    ]
