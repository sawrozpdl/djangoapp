# Generated by Django 3.0 on 2019-12-09 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.IntegerField(default='hE862', max_length=5, primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField(max_length=300)),
                ('deletedAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('tid', models.IntegerField(default='VIJlDlzN', max_length=8, primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=500)),
                ('content', models.TextField(max_length=65000)),
                ('dateCreated', models.DateTimeField()),
                ('dateModified', models.DateTimeField()),
                ('deletedAt', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.User')),
            ],
        ),
    ]
