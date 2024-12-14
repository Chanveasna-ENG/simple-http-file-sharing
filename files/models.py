from django.db import models

# Create your models here.
# import os

# class SharedFile(models.Model):
#     file = models.FileField(upload_to='shared_folder/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.file.name

# files/models.py
from django.db import models
import uuid

class ApprovedDevice(models.Model):
    device_token = models.UUIDField(default=uuid.uuid4, unique=True)
    device_name = models.CharField(max_length=200)
    ip_address = models.GenericIPAddressField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.device_name} ({self.ip_address})"