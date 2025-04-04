# Generated by Django 5.0 on 2024-11-12 18:20

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_ru', models.CharField(max_length=100, null=True)),
                ('name_uz', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('bitrix_product_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200, null=True)),
                ('name_ru', models.CharField(max_length=200, null=True)),
                ('name_uz', models.CharField(max_length=200, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_uz', models.TextField(null=True)),
                ('size', models.CharField(max_length=50)),
                ('size_en', models.CharField(max_length=50, null=True)),
                ('size_ru', models.CharField(max_length=50, null=True)),
                ('size_uz', models.CharField(max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('min_amount', models.PositiveIntegerField()),
                ('material', models.CharField(max_length=100)),
                ('material_en', models.CharField(max_length=100, null=True)),
                ('material_ru', models.CharField(max_length=100, null=True)),
                ('material_uz', models.CharField(max_length=100, null=True)),
                ('warming_material', models.CharField(max_length=100)),
                ('warming_material_en', models.CharField(max_length=100, null=True)),
                ('warming_material_ru', models.CharField(max_length=100, null=True)),
                ('warming_material_uz', models.CharField(max_length=100, null=True)),
                ('filling', models.CharField(max_length=100)),
                ('filling_en', models.CharField(max_length=100, null=True)),
                ('filling_ru', models.CharField(max_length=100, null=True)),
                ('filling_uz', models.CharField(max_length=100, null=True)),
                ('hood', models.CharField(max_length=100)),
                ('hood_en', models.CharField(max_length=100, null=True)),
                ('hood_ru', models.CharField(max_length=100, null=True)),
                ('hood_uz', models.CharField(max_length=100, null=True)),
                ('availability', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name_request', models.CharField(max_length=255)),
                ('phone_number_request', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='store.product')),
            ],
        ),
    ]
