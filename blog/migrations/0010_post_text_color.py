# Generated by Django 4.0.2 on 2022-03-11 15:56

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_color',
            field=colorfield.fields.ColorField(default='#000000', image_field=None, max_length=18, samples=None),
        ),
    ]
