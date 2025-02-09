# Generated by Django 5.0.1 on 2024-03-29 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("affiliate", "__first__"),
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="reffered_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reffered_users",
                to="affiliate.affiliate",
            ),
        ),
    ]
