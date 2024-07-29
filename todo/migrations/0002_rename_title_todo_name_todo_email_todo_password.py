# Generated by Django 4.2.14 on 2024-07-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='todo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
