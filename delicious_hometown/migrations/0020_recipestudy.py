# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-11 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delicious_hometown', '0019_recipematerial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delicious_hometown.RecipeLevel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delicious_hometown.User')),
            ],
            options={
                'db_table': 'RecipeStudy',
            },
        ),
    ]