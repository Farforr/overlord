from django.contrib import admin
from .models import Minion, MinionRequest, MinionRequestHeader, MinionRequestBody, MinionData

class MinionInline(admin.TabularInline):
    model = Minion
    fieldsets = [
        ('Overview', {'fields': ('name',)})
    ]
    extra = 3

class MinionRequestInline(admin.TabularInline):
    model = MinionRequest
    extra = 3

class MinionRequestHeaderInline(admin.TabularInline):
    model = MinionRequestHeader
    extra = 3
    verbose_name_plural = "Headers"

class MinionRequestBodyInline(admin.TabularInline):
    model = MinionRequestBody
    extra = 1
    verbose_name_plural = "Body"

@admin.register(Minion)
class MinionAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'last_modified']
    fieldsets = [
        ('Overview', {'fields': ['name', 'owner', 'parent']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]
    inlines = [MinionInline]


    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.owner = request.user
            instance.save()
        formset.save_m2m()

@admin.register(MinionRequest)
class MinionRequestAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'last_modified']
    fieldsets = [
        ('Overview', {'fields': ['owner', 'direction', 'response']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]
    inlines = [MinionRequestHeaderInline, MinionRequestBodyInline]

@admin.register(MinionRequestHeader)
class MinionRequestHeaderAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'last_modified']
    fieldsets = [
        ('Overview', {'fields': ['request', 'name', 'value']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]

@admin.register(MinionRequestBody)
class MinionRequestBodyAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'last_modified']
    fieldsets = [
        ('Overview', {'fields': ['request', 'value']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]

@admin.register(MinionData)
class MinionRequestBodyAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'last_modified']
    fieldsets = [
        ('Overview', {'fields': ['minion', 'request', 'field_name', 'field_value']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]

