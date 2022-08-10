# Generated by Django 4.0.3 on 2022-08-11 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_img'),
        ('file', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUse',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file.file')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'file_use',
            },
        ),
    ]