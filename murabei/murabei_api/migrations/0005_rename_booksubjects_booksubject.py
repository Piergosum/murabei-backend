# Generated by Django 4.2.3 on 2023-07-28 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('murabei_api', '0004_remove_booksubjects_book_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookSubjects',
            new_name='BookSubject',
        ),
    ]
