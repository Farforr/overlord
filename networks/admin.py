from django.contrib import admin

from .models import Network
from devices.admin import NodeInline


class abstractAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'last_modified']
    fieldsets = [
        ('Basic Information', {'fields': ['name']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]


class NetworkAdmin(abstractAdmin):
    inlines = [NodeInline]


admin.site.register(Network, NetworkAdmin)
