from django.contrib import admin
from django.urls import path, include
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('backend.urls', namespace='backend')),
]
