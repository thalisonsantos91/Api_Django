# Generated by Django 4.2.4 on 2025-03-29 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'categoria',
            },
        ),
    ]
