# Generated by Django 4.2.1 on 2023-05-06 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('author', models.CharField(max_length=200, unique=True)),
                ('language', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=200)),
                ('number_of_pages', models.FloatField()),
                ('price', models.FloatField()),
                ('barcode', models.FloatField()),
                ('stock', models.IntegerField()),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('image', models.ImageField(upload_to='photos/products')),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
