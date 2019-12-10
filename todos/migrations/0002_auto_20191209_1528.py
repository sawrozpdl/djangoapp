# Generated by Django 3.0 on 2019-12-09 15:28

from django.db import migrations, models
import utils.random


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='tid',
            field=models.IntegerField(default=utils.random.genId, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.IntegerField(default=utils.random.genId, max_length=5, primary_key=True, serialize=False),
        ),
    ]
