# Generated by Django 4.1.5 on 2023-01-13 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courseapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="crs_name",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Course Name"
            ),
        ),
    ]
