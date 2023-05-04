# Generated by Django 4.1.8 on 2023-05-04 19:53

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('content', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())])), ('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.CharBlock(max_length=50)), ('code', wagtail.blocks.TextBlock())]))], blank=True, null=True, use_json_field=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
