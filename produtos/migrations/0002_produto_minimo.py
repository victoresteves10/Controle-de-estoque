# Generated by Django 4.1.7 on 2023-04-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='minimo',
            field=models.DecimalField(decimal_places=1, default=10, max_digits=10),
            preserve_default=False,
        ),
    ]
