# Generated by Django 5.0 on 2024-07-27 06:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_alter_price_frequency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='price',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='price',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='plan',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='price',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='price',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
