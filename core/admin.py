from django.contrib import admin


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
