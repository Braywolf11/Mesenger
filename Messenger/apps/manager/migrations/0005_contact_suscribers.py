# Generated by Django 2.2.5 on 2019-10-05 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_social_web'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation_date')),
                ('modify_date', models.DateField(auto_now=True, verbose_name='Modify_date')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Delete_date')),
                ('first_name', models.CharField(max_length=100, verbose_name='First_name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last_name')),
                ('email', models.EmailField(max_length=150, verbose_name='E-mail')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('messaje', models.TextField(verbose_name='Messaje')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='suscribers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation_date')),
                ('modify_date', models.DateField(auto_now=True, verbose_name='Modify_date')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Delete_date')),
                ('email', models.EmailField(max_length=150, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Suscriber',
                'verbose_name_plural': 'Suscribers',
            },
        ),
    ]
