# Generated by Django 4.0.2 on 2022-07-08 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0002_file_postar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='titulo',
            field=models.CharField(max_length=200, null=True),
        ),
    ]