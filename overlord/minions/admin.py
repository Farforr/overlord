from django.contrib import admin
from .models import Minion, MinionData


class MinionInline(admin.TabularInline):
    model = Minion
    fieldsets = [
        ('Overview', {'fields': ('name',)})
    ]
    extra = 3


class MinionDataInline(admin.TabularInline):
    model = MinionData
    fields = ('field_name', 'field_value')
    extra = 3


@admin.register(Minion)
class MinionAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'last_modified']
    fieldsets = [
        ('Overview', {'fields': ['name', 'owner', 'parent']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]
    inlines = [MinionInline, MinionDataInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.owner = request.user
            instance.save()
        formset.save_m2m()


@admin.register(MinionData)
class MinionDataAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'last_modified']
    fieldsets = [
        ('Overview', {'fields': [
         'minion', 'request', 'field_name', 'field_value']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]
