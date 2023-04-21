# Generated by Django 4.2 on 2023-04-18 23:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do produto')),
                ('descricao', models.TextField()),
                ('preco', models.IntegerField()),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('categoria', models.CharField(max_length=200)),
                ('foto_produto', models.ImageField(upload_to='fotos/%d/%m/%Y/')),
                ('data_produto', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
