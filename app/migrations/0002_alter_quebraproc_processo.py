# Generated by Django 3.2.2 on 2021-09-13 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quebraproc',
            name='processo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.processo'),
        ),
    ]
