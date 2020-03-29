# Generated by Django 2.2.3 on 2019-12-20 14:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="AppSetting",
            fields=[
                ("active", models.BooleanField(primary_key=True, serialize=False)),
                ("next_hint", models.DateTimeField(default=0)),
                ("last_max_level", models.IntegerField(default=1)),
                ("max_level", models.IntegerField(default=1)),
                ("use_alternative_map", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="HintTime",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="HuntEvent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("REQ", "Hint requested"),
                            ("REL", "Hints released"),
                            ("ADV", "Advanced level"),
                        ],
                        max_length=3,
                    ),
                ),
                ("team", models.CharField(default="", max_length=127)),
                ("level", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Level",
            fields=[
                ("number", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=5000)),
                ("latitude", models.DecimalField(decimal_places=7, max_digits=13)),
                ("longitude", models.DecimalField(decimal_places=7, max_digits=13)),
                ("tolerance", models.IntegerField()),
                ("clues", models.CharField(max_length=500)),
                ("hints_shown", models.IntegerField(default=1)),
                ("hint_requested", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="HuntInfo",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("level", models.IntegerField(default=1)),
                ("hint_requested", models.BooleanField(default=False)),
                ("private_hint_requested", models.BooleanField(default=False)),
                ("private_hints_shown", models.IntegerField(default=0)),
                ("private_hint_allowed", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
