# Generated by Django 4.0.2 on 2022-03-12 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_text_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postimage',
            field=models.ImageField(blank=True, default='blank.png', null=True, upload_to='post_images'),
        ),
    ]
