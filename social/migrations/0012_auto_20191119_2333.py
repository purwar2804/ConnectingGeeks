# Generated by Django 2.2.7 on 2019-11-19 18:03

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
