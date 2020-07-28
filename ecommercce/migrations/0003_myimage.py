# Generated by Django 3.0.7 on 2020-07-21 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommercce', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('img', models.ImageField(default='', upload_to='media')),
            ],
            options={
                'db_table': 'MyImage',
            },
        ),
    ]