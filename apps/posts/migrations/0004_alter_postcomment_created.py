# Generated by Django 4.1.7 on 2023-02-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_postcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания комментария'),
        ),
    ]
