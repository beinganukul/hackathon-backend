# Generated by Django 4.0.4 on 2022-04-28 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_alter_newuser_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='book',
            field=models.ManyToManyField(blank=True, to='api_app.books'),
        ),
    ]
