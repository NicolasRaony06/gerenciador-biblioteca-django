# Generated by Django 5.0.7 on 2024-07-24 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("funcionarios", "0001_initial"),
        ("livros", "0003_alter_autor_foto_autor_alter_editora_foto_editora"),
    ]

    operations = [
        migrations.CreateModel(
            name="Livro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=150)),
                ("isbn", models.CharField(max_length=20, unique=True)),
                ("data_publicacao", models.DateField()),
                ("numero_paginas", models.PositiveIntegerField()),
                ("numero_amostras", models.PositiveBigIntegerField(default=0)),
                ("descricao", models.TextField(blank=True)),
                (
                    "capa",
                    models.ImageField(
                        default="livros_capas/default.jpeg", upload_to="livros_capas"
                    ),
                ),
                ("data_cadastro", models.DateTimeField(auto_now_add=True)),
                ("data_ultima_atualizacao", models.DateTimeField(auto_now=True)),
                (
                    "autor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="livros.autor"
                    ),
                ),
                (
                    "editora",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="livros.editora"
                    ),
                ),
                (
                    "funcionario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="funcionarios.dadosfuncionario",
                    ),
                ),
            ],
        ),
    ]
