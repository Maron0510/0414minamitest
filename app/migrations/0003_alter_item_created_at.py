# Generated by Django 4.2 on 2023-04-20 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='製造日'),
        ),
    ]