# Generated by Django 4.0.2 on 2022-07-05 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0005_alter_estagio_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='estagio',
            name='postar',
            field=models.BooleanField(default=False),
        ),
    ]
