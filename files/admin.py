from django.contrib import admin

# Register your models here.
# files/admin.py
from django.contrib import admin
from .models import ApprovedDevice

@admin.register(ApprovedDevice)
class ApprovedDeviceAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'ip_address', 'approved', 'created_at', 'last_used')
    list_filter = ('approved',)
    search_fields = ('device_name', 'ip_address')
    readonly_fields = ('device_token', 'created_at', 'last_used')
    list_editable = ('approved',)
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('ip_address',)
        return self.readonly_fields