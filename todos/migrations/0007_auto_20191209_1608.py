# Generated by Django 3.0 on 2019-12-09 16:08

from django.db import migrations, models
import utils.random


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_auto_20191209_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='tid',
            field=models.CharField(blank=True, default=utils.random.genId, max_length=12, primary_key=True, serialize=False),
        ),
    ]
