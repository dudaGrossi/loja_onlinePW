# Generated by Django 5.1.4 on 2025-01-10 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_alter_produto_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='codigo',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]
