# Generated by Django 4.2.14 on 2024-07-30 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0003_alter_todo_email_alter_todo_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], default='low', max_length=10),
        ),
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]