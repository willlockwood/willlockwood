from django.db import models
from django.contrib import admin
from datetime import datetime
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

# class Court(models.Model):
#     name = models.CharField(max_length=100, blank=True, null=True)
#
#     def __str__(self):
#         return self.name

class Justice(models.Model):
    cj = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(default=2019, blank=True, null=True)
    def __str__(self):
        if self.cj == 'CJ':
            return self.cj + ' ' + self.last_name
            # + ' (' + String(self.start_year) + '-' + string(self.end_year) + ')'
        else:
            return self.last_name
            # + ' (' + String(self.start_year) + '-' + String(self.end_year) + ')'

    class Meta:
        ordering = ['last_name']


class Judge(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class LawClass(models.Model):
    law_class = models.CharField(max_length=100, primary_key=True)
    description = models.TextField()

    def __str__(self):
        return self.law_class

class CaseTopic(models.Model):
    topic = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.topic

class CaseSubTopic(models.Model):
    sub_topic = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.sub_topic

class Case(models.Model):
    case_name = models.CharField(max_length=100)

    related_case = models.ManyToManyField('self', default=None, blank=True)
    year = models.IntegerField()

    maj_opinion = models.ManyToManyField(Justice, related_name='maj_opinion', db_column='maj_opinion', default=None, blank=True)
    maj_joined = models.ManyToManyField(Justice, related_name='maj_joined', db_column='maj_joined', default=None, blank=True)
    dissent_opinion = models.ManyToManyField(Justice, related_name='dissent_opinion', db_column='dissent_opinion', default=None, blank=True)
    dissent_joined = models.ManyToManyField(Justice, related_name='dissent_joined', db_column='dissent_joined', default=None, blank=True)

    importance = models.TextField(blank=True)
    facts = models.TextField(blank=True)
    issues = models.TextField(blank=True)
    arguments = models.TextField(blank=True)
    ruling = models.TextField(blank=True)
    discussion = models.TextField(blank=True)

    concur_opinion = models.ManyToManyField(Justice, related_name='concur_opinion', db_column='concur_opinion', default=None, blank=True)
    concur_joined = models.ManyToManyField(Justice, related_name='concur_joined', db_column='concur_joined', default=None, blank=True)
    concur2_opinion = models.ManyToManyField(Justice, related_name='concur2_opinion', db_column='concur2_opinion', default=None, blank=True)
    concur2_joined = models.ManyToManyField(Justice, related_name='concur2_joined', db_column='concur2_joined', default=None, blank=True)
    concur3_opinion = models.ManyToManyField(Justice, related_name='concur3_opinion', db_column='concur3_opinion', default=None, blank=True)
    concur3_joined = models.ManyToManyField(Justice, related_name='concur3_joined', db_column='concur3_joined', default=None, blank=True)

    dissent2_opinion = models.ManyToManyField(Justice, related_name='dissent2_opinion', db_column='dissent2_opinion', default=None, blank=True)
    dissent2_joined = models.ManyToManyField(Justice, related_name='dissent2_joined', db_column='dissent2_joined', default=None, blank=True)
    dissent3_opinion = models.ManyToManyField(Justice, related_name='dissent3_opinion', db_column='dissent3_opinion', default=None, blank=True)
    dissent3_joined = models.ManyToManyField(Justice, related_name='dissent3_joined', db_column='dissent3_joined', default=None, blank=True)
    justices_np = models.ManyToManyField(Justice, related_name='justices_np', db_column='justices_np', default=None, blank=True)

    topic = models.ManyToManyField(CaseTopic)
    sub_topic = models.ManyToManyField(CaseSubTopic, blank=True)

    law_class = models.ForeignKey(LawClass, default=None, blank=True, null=True, db_column='law_class', on_delete=models.CASCADE)
    law_classes = models.ManyToManyField(LawClass, related_name='law_classes')

    def yearReturn(self):
        return self.year

    def __str__(self):
        return self.case_name
