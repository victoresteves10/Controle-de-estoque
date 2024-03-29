# Generated by Django 4.1.7 on 2023-04-16 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_alter_produto_medida'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='armazenamento',
            field=models.CharField(choices=[('aberto', 'aberto'), ('estoque', 'estoque')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='marca',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
