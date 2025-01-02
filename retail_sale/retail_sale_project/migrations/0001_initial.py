# Generated by Django 5.0.1 on 2024-07-26 08:44

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=100)),
                ('district_status', models.BooleanField(default=False)),
                ('district_created_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Species_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species_category_name', models.CharField(max_length=100)),
                ('species_category_status', models.BooleanField(default=False)),
                ('species_category_created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('district_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='retail_sale_project.district')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species_name', models.CharField(max_length=100)),
                ('species_quantity', models.CharField(max_length=100)),
                ('species_sub_quantity', models.CharField(max_length=100)),
                ('species_date', models.DateField()),
                ('species_depots', models.CharField(max_length=100)),
                ('species_address_line_1', models.CharField(max_length=100)),
                ('species_address_line_2', models.CharField(max_length=100)),
                ('species_phone_number', models.CharField(max_length=100)),
                ('species_email', models.EmailField(max_length=254)),
                ('species_status', models.BooleanField(default=False)),
                ('species_created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('district_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='retail_sale_project.district')),
                ('species_category_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='retail_sale_project.species_category')),
            ],
        ),
    ]