from django.urls import path
from . import views

urlpatterns = [
    path('scan/<str:user>', views.privacy_check, name="privado-privacy-check"),
    path('result/<str:user>/<str:filename>', views.get_privacy_scan_result, name="privado-privacy-scan-get")
]