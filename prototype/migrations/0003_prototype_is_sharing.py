# Generated by Django 4.0.3 on 2022-08-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0002_alter_page_pagecanvasstyle'),
    ]

    operations = [
        migrations.AddField(
            model_name='prototype',
            name='is_sharing',
            field=models.BooleanField(default=False),
        ),
    ]
