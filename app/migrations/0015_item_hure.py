# Generated by Django 4.1.7 on 2023-05-06 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_item_age_remove_item_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='hure',
            field=models.CharField(default='a', max_length=200, verbose_name='フレーム'),
        ),
    ]
