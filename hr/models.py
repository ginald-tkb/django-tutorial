from __future__ import unicode_literals

from django.contrib import admin
from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('frontend', 'Front End Developer'),
    ('backend', 'Back End Developer'),
    ('pm', 'Project Manager'),
    ('analyst', 'Business Analyst'),
    ('hr', 'HR Consultant'),
)

class Task(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    due_date = models.DateTimeField('Due Date')

    def __unicode__(self):
        return '%s' % self.title

class Skill(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

class Job(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(null=True)
    mission = models.TextField(null=True)
    category = models.CharField(max_length=255, db_index=True, choices=CATEGORY_CHOICES) # default="frontend", unique=True,
    location = models.CharField(max_length=100, null=True)
    posted = models.DateField(blank=False, null=False)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    is_active = models.BooleanField('Is Active', default=True)
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)

    def __unicode__(self):
        return '%s' % self.title

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date')

class SkillAdmin(admin.ModelAdmin):
    pass

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active')
    list_filter = ('category',)
    ordering = ('-created',)
