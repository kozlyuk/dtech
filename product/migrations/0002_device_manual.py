# Generated by Django 5.0.4 on 2024-04-04 09:05

import product.formatChecker
import product.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='manual',
            field=product.formatChecker.ContentTypeRestrictedFileField(blank=True, null=True, upload_to=product.models.docs_directory_path, verbose_name='Електронний примірник'),
        ),
    ]
