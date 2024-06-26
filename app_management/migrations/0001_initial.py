# Generated by Django 4.2.11 on 2024-06-28 23:54

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Changelog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", markdownx.models.MarkdownxField()),
                ("version", models.CharField(max_length=50)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
