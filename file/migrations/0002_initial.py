# Generated by Django 4.0.6 on 2022-08-07 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file', '0001_initial'),
        ('user', '0001_initial'),
        ('project', '0001_initial'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AddField(
            model_name='file',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.team'),
        ),
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
