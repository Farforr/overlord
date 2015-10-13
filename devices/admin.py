from django.contrib import admin

from .models import Node, SensorType, ActuatorType, Sensor, Actuator, SensorData, ActuatorData

"""Inlines"""


class NodeInline(admin.TabularInline):
    model = Node
    extra = 3


class SensorInline(admin.TabularInline):
    model = Sensor
    extra = 3


class ActuatorInline(admin.TabularInline):
    model = Actuator
    extra = 3


class SensorDataInline(admin.TabularInline):
    model = SensorData
    extra = 0


class ActuatorDataInline(admin.TabularInline):
    model = ActuatorData

"""End Inlines"""


class abstractAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'last_modified']
    fieldsets = [
        ('Basic Information', {'fields': ['name']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]

class NodeAdmin(abstractAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['name', 'network']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]
    list_display = ['name', 'network', 'created', 'last_modified']
    inlines = [SensorInline, ActuatorInline]
    list_filter = ['network']
    search_fields = ['name', 'network']


class SensorAdmin(abstractAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['name', 'model', 'node']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]
    list_display = ['name', 'node', 'created', 'last_modified']
    inlines = [SensorDataInline]
    list_filter = ['node']
    search_fields = ['name', 'node']


class ActuatorAdmin(abstractAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['name', 'model', 'node']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]
    list_display = ['name', 'node', 'created', 'last_modified']
    inlines = [ActuatorDataInline]
    list_filter = ['node']
    search_fields = ['name', 'node']

admin.site.register(Node, NodeAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Actuator, ActuatorAdmin)
admin.site.register(SensorType)
admin.site.register(ActuatorType)
admin.site.register(SensorData)
admin.site.register(ActuatorData)
