# Generated by Django 5.1.4 on 2024-12-04 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='produto',
        ),
    ]
