# Generated by Django 4.0 on 2024-05-21 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_alter_condominiumdocuments_doc_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdocuments',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]