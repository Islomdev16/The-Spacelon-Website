# Generated by Django 3.2.6 on 2021-08-18 20:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='piks')),
                ('title', models.CharField(max_length=200)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField()),
            ],
        ),
    ]
