# Generated by Django 2.1.2 on 2018-10-15 13:07

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_url', models.URLField()),
                ('due_date', models.DateTimeField(default=core.models.return_date_time)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'clientele',
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='clientele',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_url', models.URLField()),
                ('business_type', models.CharField(choices=[('Blog', 'blog'), ('Youtube', 'youtube'), ('Local Business', 'local_business'), ('Other', 'other')], default='Blog', max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'clientele',
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]
