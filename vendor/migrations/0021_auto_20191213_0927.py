# Generated by Django 2.2.5 on 2019-12-13 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0020_auto_20191212_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_pic',
            field=models.ImageField(blank=True, upload_to='static/vendor/images'),
        ),
    ]
