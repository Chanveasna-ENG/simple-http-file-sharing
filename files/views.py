# files/views.py
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse

def file_list(request):
    """List all files in the shared folder"""
    shared_folder = settings.SHARED_FOLDER
    
    try:
        files = os.listdir(shared_folder)
    except PermissionError:
        return HttpResponse("Permission denied to access shared folder", status=403)
    except FileNotFoundError:
        return HttpResponse("Shared folder not found", status=404)
    
    if request.method == 'POST' and request.FILES.get('file'):
        # Handle file upload
        uploaded_file = request.FILES['file']
        file_path = os.path.join(shared_folder, uploaded_file.name)
        
        # Save the uploaded file
        try:
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            return redirect('file_list')
        except PermissionError:
            return HttpResponse("Permission denied to write file", status=403)
    
    return render(request, 'file_upload.html', {
        'files': files,
        'shared_folder': shared_folder
    })

def download_file(request, filename):
    """Download a file from the shared folder"""
    shared_folder = settings.SHARED_FOLDER
    file_path = os.path.join(shared_folder, filename)
    
    if os.path.exists(file_path):
        try:
            response = FileResponse(open(file_path, 'rb'))
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
        except PermissionError:
            return HttpResponse('Permission denied to read file', status=403)
    else:
        return HttpResponse('File not found', status=404)


# files/views.py
# Add these new views
from .models import ApprovedDevice
from django.contrib.admin.views.decorators import staff_member_required

def request_access(request):
    if request.method == 'POST':
        device_name = request.POST.get('device_name')
        device = ApprovedDevice.objects.create(
            device_name=device_name,
            ip_address=request.META.get('REMOTE_ADDR')
        )
        response = render(request, 'files/waiting_approval.html')
        response.set_cookie('device_token', str(device.device_token))
        return response
    return render(request, 'files/request_access.html')

@staff_member_required
def approve_device(request):
    pending_devices = ApprovedDevice.objects.filter(approved=False)
    if request.method == 'POST':
        device_id = request.POST.get('device_id')
        action = request.POST.get('action')
        
        device = ApprovedDevice.objects.get(id=device_id)
        if action == 'approve':
            device.approved = True
            device.save()
        elif action == 'deny':
            device.delete()
            
    return render(request, 'files/approve_devices.html', {
        'pending_devices': pending_devices
    })

# files/views.py
from django.contrib.auth.decorators import login_required

@login_required
def approve_devices(request):
    devices = ApprovedDevice.objects.all().order_by('-created_at')
    return render(request, 'files/approve_devices.html', {
        'devices': devices
    })