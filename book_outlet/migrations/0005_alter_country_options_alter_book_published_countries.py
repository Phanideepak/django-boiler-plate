# Generated by Django 5.1.3 on 2024-11-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0004_country_alter_address_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Country Entries'},
        ),
        migrations.AlterField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(related_name='books', to='book_outlet.country'),
        ),
    ]
