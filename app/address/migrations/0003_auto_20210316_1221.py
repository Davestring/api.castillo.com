# Generated by Django 3.1.7 on 2021-03-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("address", "0002_auto_20210316_1144")]

    operations = [
        migrations.AlterField(
            model_name="addressmodel",
            name="references",
            field=models.TextField(blank=True),
        )
    ]