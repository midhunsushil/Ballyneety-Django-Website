# Generated by Django 4.0.2 on 2022-02-13 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_content', '0005_alter_post_options_alter_postgallery_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postgallery',
            options={'ordering': ('post__title',), 'verbose_name': 'postgallery', 'verbose_name_plural': 'post gallery'},
        ),
    ]
