# Generated by Django 5.1.5 on 2025-01-28 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_alter_produto_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='pedido_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
