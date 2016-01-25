from django.contrib import admin
from .models import Node
from overlord.networks.models import Network


class NodeInline(admin.TabularInline):
    model = Node
    extra = 3


class abstractAdmin(admin.ModelAdmin):
    # I dont know why, but if the admin imports this class, everything breaks
    # so for now I have to keep it duplicated :(
    readonly_fields = ['created', 'last_modified']
    fieldsets = [
        ('Basic Information', {'fields': ['name']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]
    inlines = []


class NodeAdmin(abstractAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['name', 'network']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]
    list_display = ['name', 'network', 'created', 'last_modified']
    list_filter = ['network']
    search_fields = ['name', 'network']


admin.site.register(Node, NodeAdmin)

# As Opposed to setting this in networks/admin.py I have elected to put this
# here instead to avoid a circular dependancy
admin.site._registry[Network].inlines.append(NodeInline)
