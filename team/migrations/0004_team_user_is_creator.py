# Generated by Django 4.0.3 on 2022-08-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_remove_team_user_is_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_user',
            name='is_creator',
            field=models.BooleanField(default=False),
        ),
    ]