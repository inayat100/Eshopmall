# Generated by Django 4.0.6 on 2022-07-30 18:42

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_product_pimage1_alter_product_pimage2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pimage1',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.uplo),
        ),
        migrations.AlterField(
            model_name='product',
            name='pimage2',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.uplo),
        ),
        migrations.AlterField(
            model_name='product',
            name='pimage3',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.uplo),
        ),
        migrations.AlterField(
            model_name='product',
            name='pimage4',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.uplo),
        ),
    ]