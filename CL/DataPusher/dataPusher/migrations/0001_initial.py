# Generated by Django 4.0.4 on 2023-01-23 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('account_id', models.CharField(max_length=255, unique=True)),
                ('account_name', models.CharField(max_length=255)),
                ('app_secret_token', models.CharField(blank=True, max_length=255)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('http_method', models.CharField(max_length=10)),
                ('headers', models.JSONField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataPusher.account')),
            ],
        ),
    ]
