# Generated by Django 4.0.2 on 2022-06-19 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField(default=18)),
                ('texto', models.TextField(blank=True, max_length=200, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('sexo', models.CharField(max_length=10, null=True)),
                ('escolaridade', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]