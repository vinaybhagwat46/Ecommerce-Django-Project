# Generated by Django 3.0.7 on 2020-07-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommercce', '0003_myimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='pimage',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
