# Generated by Django 5.0.4 on 2024-07-15 17:43

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_device_creator'),
        ('structure', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='short_description',
        ),
        migrations.AddField(
            model_name='device',
            name='executor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='structure.contractor', verbose_name='Executor'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='configuration_creators', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата')),
                ('event', models.CharField(choices=[('IS', 'Issued for work'), ('AC', 'Accepted from producer'), ('CO', 'Configured'), ('TE', 'Tested'), ('SE', 'Sent to customer'), ('RE', 'Rejected'), ('FI', 'Fixed')], default='IS', max_length=2, verbose_name='Event')),
                ('comment', models.CharField(max_length=255, verbose_name='Comment')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.device', verbose_name='Device')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['-date'],
            },
        ),
    ]
