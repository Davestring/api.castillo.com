# Generated by Django 3.1.7 on 2021-03-17 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("comment", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="commentmodel",
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
            },
        ),
        migrations.RenameField(
            model_name="commentmodel", old_name="createdAt", new_name="created"
        ),
        migrations.RenameField(
            model_name="commentmodel", old_name="updatedAt", new_name="updated"
        ),
    ]