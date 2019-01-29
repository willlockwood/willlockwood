from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import LawClass, CaseTopic, CaseSubTopic, Case, Judge, Justice
# , Court

# Register your models here.

@admin.register(LawClass)
class LawClass(admin.ModelAdmin):
    list_display = ['law_class', 'description']

    class Meta:
        model = LawClass

@admin.register(CaseTopic)
class CaseTopic(admin.ModelAdmin):
    list_display = ['topic']

    class Meta:
        model = CaseTopic

@admin.register(CaseSubTopic)
class CaseSubTopic(admin.ModelAdmin):
    list_display = ['sub_topic']

    class Meta:
        model = CaseSubTopic

@admin.register(Case)
class Case(ImportExportModelAdmin):
    list_display = ['case_name', 'year', 'law_class']

    class Meta:
        model = Case

@admin.register(Justice)
class Justice(ImportExportModelAdmin):
    list_display = ['__str__', 'cj']

    class Meta:
        model = Justice
        ordering = ['__str__']

@admin.register(Judge)
class Judge(ImportExportModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "name":
            kwargs["queryset"] = Judge.objects.order_by('name')
        return super(MyModelAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


# @admin.register(Court)
# class Court(admin.ModelAdmin):
#     def formfield_for_manytomany(self, db_field, request, **kwargs):
#         if db_field.name == "name":
#             kwargs["queryset"] = Court.objects.order_by('name')
#         return super(MyModelAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    # class Meta:
    #     model = Judge
