# Generated by Django 5.0.12 on 2025-02-12 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closures', '0011_create_closures_origem_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='closing',
            name='observation',
            field=models.TextField(blank=True, null=True, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='closing',
            name='document_date',
            field=models.DateField(blank=True, null=True, verbose_name='DATA DO DOC.'),
        ),
    ]
