# Generated by Django 4.2 on 2023-05-12 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_author_alter_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='number_of_pages',
            field=models.IntegerField(),
        ),
    ]