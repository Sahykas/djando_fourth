# Generated by Django 4.2 on 2023-04-27 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]