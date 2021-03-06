# Generated by Django 4.0.2 on 2022-06-22 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import file_upload.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to=file_upload.models.user_directory_path)),
                ('titulo', models.CharField(max_length=20, null=True)),
                ('texto', models.TextField(blank=True, max_length=1000, null=True)),
                ('equipe', models.TextField(max_length=200, null=True)),
                ('turma', models.CharField(max_length=20, null=True)),
                ('curso', models.CharField(max_length=20, null=True)),
                ('orientador', models.CharField(max_length=20, null=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('excluir', 'editar'), ('editar', 'editar'), ('criar', 'criar')),
            },
        ),
    ]
