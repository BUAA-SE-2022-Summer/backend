# Generated by Django 4.0.3 on 2022-08-11 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_is_sharing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_sharing',
            field=models.BooleanField(default=False),
        ),
    ]