# Generated by Django 3.2.4 on 2021-08-24 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_rename_catalogo_catalogos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Catalogos',
        ),
    ]
