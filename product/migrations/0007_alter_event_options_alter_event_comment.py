# Generated by Django 5.0.4 on 2024-07-16 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_device_short_description_device_executor_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-date', 'pk'], 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterField(
            model_name='event',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Comment'),
        ),
    ]
