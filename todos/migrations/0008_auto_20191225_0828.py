# Generated by Django 3.0 on 2019-12-25 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_auto_20191209_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(blank=True, default='', max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='tag',
            field=models.ManyToManyField(to='todos.Tag'),
        ),
    ]
