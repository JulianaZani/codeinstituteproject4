from django.contrib import admin
from django.urls import path, include
from accounts.views import signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testimonials.urls')),
    path('accounts/signup/', signup_view, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]