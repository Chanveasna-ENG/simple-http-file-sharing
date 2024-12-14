# files/urls.py
from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.file_list, name='file_list'),
#     path('download/<str:filename>/', views.download_file, name='download_file'),
# ]

# files/urls.py
from django.urls import path
from . import views

# files/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('download/<str:filename>/', views.download_file, name='download_file'),
    path('request-access/', views.request_access, name='request_access'),
    # path('approve-devices/', views.approve_devices, name='approve_devices'),
]