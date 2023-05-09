# Generated by Django 4.1.8 on 2023-05-09 02:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0009_blogtag_taggedblog_blogpage_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogtag",
            name="color",
        ),
        migrations.AddField(
            model_name="blogtag",
            name="border_color",
            field=models.CharField(
                blank=True,
                help_text="A CSS color for the tag border",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="blogtag",
            name="text_color",
            field=models.CharField(
                blank=True,
                help_text="A CSS color for the tag text",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="blogtag",
            name="background_color",
            field=models.CharField(
                blank=True,
                help_text="A CSS color for the tag background",
                max_length=50,
                null=True,
            ),
        ),
    ]