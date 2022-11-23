from django.urls import path, include
from django.conf import settings
from .views import *



urlpatterns = [
    path('Admin_login_page', Admin_login_page, name="Admin_login_page"),
    path('Admin_logout', Admin_logout, name="Admin_logout"),
    path('Admin_dashboard', Admin_dashboard, name="Admin_dashboard"),
    # path('Capture_image', Capture_image, name = "Capture_image")
    path('testing', testing, name="testing"),
    path('saveImage/', saveImage, name="saveImage")
] 
