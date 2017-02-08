from rest_framework import serializers
from django.contrib.auth.models import User, Group
from hr.models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('url', 'pk', 'title')


class JobSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    class Meta:
        model = Job
        fields = ('url', 'pk', 'title', 'description', 'mission', 'category', 'location', 'posted', 'is_active', 'skills')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
