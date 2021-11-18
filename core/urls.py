from example import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('normalRequests', views.test_normal_requests, name="test_normal_requests"),
    path('aiohttpRequests', views.test_aiohttp_requests, name="test_aiohttp_requests"),
    path('asyncRequests', views.test_async_requests, name="test_async_requests")
]
