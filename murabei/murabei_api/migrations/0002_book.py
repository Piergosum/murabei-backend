# Generated by Django 4.2.3 on 2023-07-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('murabei_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author_id', models.IntegerField()),
                ('title_slug', models.TextField(unique=True)),
                ('price', models.TextField()),
                ('format', models.TextField()),
                ('publisher', models.TextField()),
                ('pubdate', models.TextField()),
                ('edition', models.TextField()),
                ('lexile', models.TextField()),
                ('pages', models.FloatField()),
                ('dimensions', models.TextField()),
                ('overview', models.TextField()),
                ('excerpt', models.TextField()),
                ('synopsis', models.TextField()),
                ('toc', models.TextField()),
                ('editorial_reviews', models.TextField()),
            ],
        ),
    ]
