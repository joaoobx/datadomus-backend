# Generated by Django 4.0 on 2024-05-23 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_alter_userdocuments_doc_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condominiumdocuments',
            name='doc_url',
            field=models.FileField(upload_to='cond_docs/'),
        ),
        migrations.AlterField(
            model_name='userdocuments',
            name='doc_url',
            field=models.FileField(upload_to='user_docs/'),
        ),
    ]
