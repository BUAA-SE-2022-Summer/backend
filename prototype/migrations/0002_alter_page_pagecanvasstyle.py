# Generated by Django 4.0.6 on 2022-08-07 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='pageCanvasStyle',
            field=models.TextField(default='{"width":1200,"height":740,"scale":100,"color":"#000","opacity":1,"background":"#fff","fontSize":14}', verbose_name='页面组件额外信息'),
        ),
    ]