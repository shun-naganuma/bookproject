# Generated by Django 3.2.8 on 2024-05-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
