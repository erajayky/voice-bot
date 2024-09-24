# Generated by Django 5.0.3 on 2024-03-12 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0006_alter_plan_features_alter_plan_github_repos_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="price",
            name="frequency",
            field=models.CharField(
                blank=True,
                choices=[
                    ("day", "day"),
                    ("week", "week"),
                    ("month", "month"),
                    ("year", "year"),
                ],
                default="month",
                max_length=10,
                null=True,
            ),
        ),
    ]
