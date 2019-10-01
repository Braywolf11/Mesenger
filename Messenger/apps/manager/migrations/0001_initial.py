# Generated by Django 2.2.5 on 2019-10-01 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation_date')),
                ('modify_date', models.DateField(auto_now=True, verbose_name='Modify_date')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Delete_date')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Category name')),
                ('image', models.ImageField(upload_to='category/', verbose_name='Category image')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]
