from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
    path('computer_vision/', include('cv_text.urls')),
    path('computer_vision/viola_jones/', include('cv_text.urls')),
]
