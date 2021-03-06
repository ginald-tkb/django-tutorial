# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-02 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField(null=True)),
                ('mission', models.TextField(null=True)),
                ('category', models.CharField(choices=[('frontend', 'Front End Developer'), ('backend', 'Back End Developer'), ('pm', 'Project Manager'), ('analyst', 'Business Analyst'), ('hr', 'HR Consultant')], db_index=True, max_length=255)),
                ('location', models.CharField(max_length=100, null=True)),
                ('posted', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('due_date', models.DateTimeField(verbose_name='Due Date')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(to='hr.Skill'),
        ),
        migrations.AddField(
            model_name='job',
            name='tasks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Task'),
        ),
    ]
