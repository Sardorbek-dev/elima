# Generated by Django 5.0 on 2024-12-09 18:33

import ckeditor.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('name_ru', models.CharField(max_length=255, null=True)),
                ('name_uz', models.CharField(max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Post Category',
                'verbose_name_plural': 'Post Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('content_en', ckeditor.fields.RichTextField(null=True)),
                ('content_ru', ckeditor.fields.RichTextField(null=True)),
                ('content_uz', ckeditor.fields.RichTextField(null=True)),
                ('author', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='img/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('show_on_homepage', models.BooleanField(default=False)),
                ('publish', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.postcategory')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
