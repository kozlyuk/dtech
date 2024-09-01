# Generated by Django 5.0.4 on 2024-09-01 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_event_options_alter_device_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='serial_number',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Serial number'),
        ),
        migrations.AlterField(
            model_name='event',
            name='device',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='product.device', verbose_name='Device'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='event',
            field=models.CharField(choices=[('IS', 'Issued for work'), ('FA', 'Frame assembly'), ('BA', 'Basic assembly'), ('FI', 'Final assembly'), ('AC', 'Accepted from producer'), ('CO', 'Configured'), ('TE', 'Tested'), ('RE', 'Rejected'), ('SE', 'Sent to customer'), ('FX', 'Fixed'), ('OT', 'Other')], default='IS', max_length=2, verbose_name='Event'),
        ),
    ]
