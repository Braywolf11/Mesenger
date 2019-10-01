# Generated by Django 2.2.5 on 2019-10-01 02:46

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20191001_0206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categorys'},
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation_date')),
                ('modify_date', models.DateField(auto_now=True, verbose_name='Modify_date')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Delete_date')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Title')),
                ('tslug', models.CharField(max_length=100, unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('image', models.ImageField(max_length=150, upload_to='images/', verbose_name='Image post')),
                ('published', models.BooleanField(default=False, verbose_name='Published / No Published')),
                ('published_date', models.DateField(verbose_name='Published date')),
                ('content', ckeditor.fields.RichTextField()),
                ('id_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.author')),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]