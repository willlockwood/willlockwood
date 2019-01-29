from django.db import models
from django.contrib import admin
from datetime import datetime
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class RuleSet(models.Model):
    set = models.CharField(max_length=100, primary_key=True)
    description = models.TextField()

    def __str__(self):
        return self.set

class Tag(models.Model):
    tag = models.CharField(max_length=35, primary_key=True)
    # slug = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

class Rule(models.Model):
    rule_number = models.IntegerField(default=None, blank=True, null=True)
    rule = models.CharField(max_length=100)
    description = models.TextField()
    set = models.ForeignKey(RuleSet, default=None, db_column='set', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.rule
