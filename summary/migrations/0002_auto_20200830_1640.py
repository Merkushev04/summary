# Generated by Django 3.1 on 2020-08-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=250)),
                ('specialization', models.CharField(max_length=250)),
                ('date_start', models.DateField(blank=True)),
                ('date_end', models.DateField(blank=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='Intro',
        ),
    ]
