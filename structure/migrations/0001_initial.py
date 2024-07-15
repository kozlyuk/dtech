# Generated by Django 5.0.4 on 2024-05-10 12:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Назва')),
                ('edrpou', models.CharField(blank=True, max_length=10, verbose_name='ЄДРПОУ')),
                ('contact_person', models.CharField(blank=True, max_length=50, verbose_name='Контактна особа')),
                ('phone', models.CharField(blank=True, max_length=13, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('requisites', models.TextField(blank=True, verbose_name='Реквізити')),
                ('active', models.BooleanField(default=True, verbose_name='Активний')),
            ],
            options={
                'verbose_name': 'Контрагент',
                'verbose_name_plural': 'Контрагенти',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Назва')),
                ('full_name', models.CharField(blank=True, max_length=100, verbose_name='Повна назва')),
                ('edrpou', models.CharField(blank=True, max_length=10, verbose_name='ЄДРПОУ')),
                ('city', models.CharField(blank=True, max_length=30, verbose_name='Місто')),
                ('legal', models.CharField(blank=True, max_length=255, verbose_name='Опис контрагента')),
                ('legal_description', models.CharField(blank=True, max_length=255, verbose_name='Організаційно-правова форма')),
                ('regulations', models.CharField(blank=True, max_length=100, verbose_name='Діє на підставі')),
                ('signatory_person', models.CharField(blank=True, max_length=50, verbose_name='Підписант')),
                ('signatory_position', models.CharField(blank=True, max_length=255, verbose_name='Посада підписанта')),
                ('requisites', models.TextField(blank=True, verbose_name='Реквізити')),
                ('bank_requisites', models.TextField(blank=True, verbose_name='Банківські реквізити')),
                ('taxation', models.CharField(choices=[('wvat', 'З ПДВ'), ('wovat', 'Без ПДВ')], default='wvat', max_length=5, verbose_name='Система оподаткування')),
                ('active', models.BooleanField(default=True, verbose_name='Активний')),
                ('accountant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='company_accountant', to=settings.AUTH_USER_MODEL, verbose_name='Бухгалтер')),
                ('chief', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='company_chiefs', to=settings.AUTH_USER_MODEL, verbose_name='Керівник')),
            ],
            options={
                'verbose_name': 'Компанія',
                'verbose_name_plural': 'Компанії',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Назва')),
                ('full_name', models.CharField(blank=True, max_length=100, verbose_name='Повна назва')),
                ('edrpou', models.CharField(blank=True, max_length=10, verbose_name='ЄДРПОУ')),
                ('city', models.CharField(blank=True, max_length=30, verbose_name='Місто')),
                ('legal', models.CharField(blank=True, max_length=255, verbose_name='Опис контрагента')),
                ('legal_description', models.CharField(blank=True, max_length=255, verbose_name='Організаційно-правова форма')),
                ('regulations', models.CharField(blank=True, max_length=100, verbose_name='Діє на підставі')),
                ('signatory_person', models.CharField(blank=True, max_length=50, verbose_name='Підписант')),
                ('signatory_position', models.CharField(blank=True, max_length=255, verbose_name='Посада підписанта')),
                ('requisites', models.TextField(blank=True, verbose_name='Реквізити')),
                ('bank_requisites', models.TextField(blank=True, verbose_name='Банківські реквізити')),
                ('contact_person', models.CharField(max_length=50, verbose_name='Контактна особа')),
                ('phone', models.CharField(max_length=13, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('debtor_term', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Термін післяоплати')),
                ('active', models.BooleanField(default=True, verbose_name='Активний')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Замовник',
                'verbose_name_plural': 'Замовники',
            },
        ),
    ]