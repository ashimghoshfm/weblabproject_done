# Generated by Django 4.1.5 on 2023-01-13 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("studentapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="st_dist",
            field=models.CharField(max_length=20, verbose_name="District"),
        ),
    ]