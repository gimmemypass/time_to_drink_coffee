# Generated by Django 3.0.5 on 2020-04-30 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200430_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique_for_date='published_date'),
        ),
    ]
