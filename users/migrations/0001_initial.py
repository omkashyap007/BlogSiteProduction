# Generated by Django 4.0.2 on 2022-03-10 03:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('about_user', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('country', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('profession', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('website_link', models.URLField(blank=True, default='', null=True)),
                ('linkedin_link', models.URLField(blank=True, default='', null=True)),
                ('twitter_link', models.URLField(blank=True, default='', null=True)),
                ('github_link', models.URLField(blank=True, default='', null=True)),
                ('instagram_link', models.URLField(blank=True, default='', null=True)),
                ('facebook_link', models.URLField(blank=True, default='', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
