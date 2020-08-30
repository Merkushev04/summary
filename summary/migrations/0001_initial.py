# Generated by Django 3.1 on 2020-08-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('information', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=250)),
                ('specialization', models.CharField(max_length=250)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=250)),
                ('contact', models.CharField(max_length=250)),
                ('message', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='foro/%Y/%m/%d')),
                ('position', models.CharField(max_length=250)),
                ('intro', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=5000)),
                ('link', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('level', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=250)),
                ('position', models.CharField(max_length=250)),
                ('duties', models.TextField(max_length=2000)),
                ('instruments', models.TextField(max_length=2000)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
            ],
        ),
    ]