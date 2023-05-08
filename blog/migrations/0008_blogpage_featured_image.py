# Generated by Django 4.1.9 on 2023-05-08 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("blog", "0007_alter_blogpage_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpage",
            name="featured_image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
    ]
