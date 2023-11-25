# Generated by Django 3.2.20 on 2023-11-22 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_teammembers_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=400, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
