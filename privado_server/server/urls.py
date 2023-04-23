from django.urls import path
from . import views

urlpatterns = [
    path('<str:user>', views.privacy_check, name="privado-privacy-check"),
]