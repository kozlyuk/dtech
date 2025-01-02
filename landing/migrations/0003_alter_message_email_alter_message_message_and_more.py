# Generated by Django 5.0.4 on 2025-01-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_alter_message_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(default='sergey.kozlyuk@gmail.com', max_length=254, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(default='message', verbose_name='Повідомлення'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='phone',
            field=models.CharField(default='0673607460', max_length=13, verbose_name='Телефон'),
            preserve_default=False,
        ),
    ]