# Generated by Django 3.2.2 on 2021-06-10 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_input_productioninput'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductionInput',
            new_name='Input',
        ),
    ]
