# Generated by Django 4.0.2 on 2022-06-29 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0004_alter_estagio_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estagio',
            options={'permissions': (('est', 'est'), ('ed', 'ed'), ('exc', 'exc'))},
        ),
    ]
