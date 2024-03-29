# Generated by Django 4.0.6 on 2022-08-07 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file', '0001_initial'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectID', models.AutoField(primary_key=True, serialize=False)),
                ('projectName', models.CharField(default='', max_length=64, verbose_name='项目名称')),
                ('projectDesc', models.TextField(default='', verbose_name='项目描述')),
                ('projectImg', models.CharField(default='', max_length=256, verbose_name='项目图片')),
                ('projectUser', models.IntegerField(default=0, verbose_name='项目创建者')),
                ('projectTime', models.DateTimeField(auto_now_add=True, verbose_name='项目创建时间')),
                ('is_star', models.BooleanField(default=False, verbose_name='是否收藏')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('root_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_root', to='file.file')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
            options={
                'db_table': 'project',
            },
        ),
    ]
