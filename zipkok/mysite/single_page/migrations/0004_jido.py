# Generated by Django 4.2.4 on 2023-09-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("single_page", "0003_authgroup_authgrouppermissions_authpermission_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Jido",
            fields=[
                (
                    "bas_id",
                    models.IntegerField(
                        blank=True,
                        db_column="BAS_ID",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "coordinates",
                    models.JSONField(blank=True, db_column="Coordinates", null=True),
                ),
            ],
            options={
                "db_table": "jido",
                "managed": False,
            },
        ),
    ]