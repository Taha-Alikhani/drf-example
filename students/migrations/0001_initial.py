# Generated by Django 4.2.4 on 2023-08-22 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('courses', models.ManyToManyField(to='courses.course')),
            ],
        ),
    ]
