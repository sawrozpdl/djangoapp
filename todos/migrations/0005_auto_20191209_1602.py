# Generated by Django 3.0 on 2019-12-09 16:02

from django.db import migrations, models
import utils.random


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_auto_20191209_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.IntegerField(blank=True, default=utils.random.genId, max_length=5, primary_key=True, serialize=False),
        ),
    ]
