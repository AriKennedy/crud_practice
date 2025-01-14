# Generated by Django 5.1.2 on 2024-11-05 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
