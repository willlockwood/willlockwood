from django.contrib import admin
from .models import Rule, Tag, RuleSet

# Register your models here.

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ['rule', 'set', 'description']
    # list_filter = ['']
    # list_display_links = ['']
    # search_fields = ['', '']
    class Meta:
        model = Rule

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']
    # list_filter = ['tag']

    class Meta:
        model = Tag
#
@admin.register(RuleSet)
class RuleSetAdmin(admin.ModelAdmin):
    list_display = ['set', 'description']

    class Meta:
        model = RuleSet
