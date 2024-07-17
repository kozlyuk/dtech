# Generated by Django 5.0.4 on 2024-07-16 17:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0004_order_deal_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_creators', to=settings.AUTH_USER_MODEL, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='order',
            name='deal_date',
            field=models.DateField(verbose_name='Deal date'),
        ),
    ]
