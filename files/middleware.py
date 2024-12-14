# files/middleware.py
from django.shortcuts import redirect
from .models import ApprovedDevice
from django.urls import reverse

class DeviceAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Paths that don't require authentication
        exempt_paths = ['/request-access/', '/approve-device/', '/admin/']
        
        if not any(request.path.startswith(path) for path in exempt_paths):
            device_token = request.COOKIES.get('device_token')
            if not device_token:
                return redirect('request_access')
            
            try:
                device = ApprovedDevice.objects.get(
                    device_token=device_token,
                    ip_address=request.META.get('REMOTE_ADDR'),
                    approved=True
                )
                device.save()  # Updates last_used timestamp
            except ApprovedDevice.DoesNotExist:
                return redirect('request_access')
                
        return self.get_response(request)