# Generated by Django 5.0.7 on 2024-07-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("livros", "0007_alter_livro_numero_amostras"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livro",
            name="numero_amostras",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
