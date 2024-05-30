# Generated by Django 4.2.7 on 2024-05-30 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
                'db_table': 'collection',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('collection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='collection.collection')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'db_table': 'item',
                'ordering': ('id',),
            },
        ),
    ]