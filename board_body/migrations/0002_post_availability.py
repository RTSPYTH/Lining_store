# Generated by Django 3.2.9 on 2021-12-08 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_body', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='availability',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
