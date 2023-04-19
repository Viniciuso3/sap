# Generated by Django 4.1.7 on 2023-03-04 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lista_produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOME_PRODUTO', models.CharField(max_length=50)),
                ('UNIDADES_VENDIDAS', models.CharField(max_length=50)),
                ('EM_ESTOQUE', models.CharField(max_length=50)),
                ('DATA_EXPIRADA', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
