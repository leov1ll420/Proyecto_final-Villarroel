# Generated by Django 4.2.7 on 2023-11-18 21:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automovil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
