# Generated by Django 4.1.7 on 2023-05-06 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_item_idou_item_kotei'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='idou',
            field=models.IntegerField(default='100', max_length=5, verbose_name='フレーム高さ移動側'),
        ),
        migrations.AlterField(
            model_name='item',
            name='kotei',
            field=models.IntegerField(default='50', max_length=5, verbose_name='フレーム高さ固定側'),
        ),
    ]