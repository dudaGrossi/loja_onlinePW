# Generated by Django 5.1.4 on 2024-12-04 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_remove_pedido_id_pedido_produto_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='produto_id',
            new_name='pedido_id',
        ),
    ]