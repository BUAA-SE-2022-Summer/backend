# Generated by Django 4.0.6 on 2022-08-07 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_edit',
            field=models.IntegerField(default=0, verbose_name='记录编辑'),
        ),
        migrations.AddField(
            model_name='project',
            name='last_modify_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
