# Generated by Django 4.1.7 on 2023-04-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_item_kanri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='kanri',
            field=models.IntegerField(choices=[('道央', '道央'), ('道南', '道南'), ('道東', '道東'), ('道北', '道北'), ('小樽', '小樽'), ('本社', '本社')], default='本社', verbose_name='管理籍'),
        ),
    ]
