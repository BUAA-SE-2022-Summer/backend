# Generated by Django 4.0.3 on 2022-08-02 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_user',
            name='is_creator',
            field=models.BooleanField(default=False),
        ),
    ]