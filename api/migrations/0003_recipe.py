# Generated by Django 4.2 on 2023-04-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_category_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('image', models.ImageField(upload_to='recipes')),
            ],
        ),
    ]
