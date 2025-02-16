"""
URL configuration for dating_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . views import error_403, error_404, error_500


handler403 = error_403
handler404 = error_404
handler500 = error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),  # path for home page
    path('questionnaire/', include('questionnaire.urls')),  # path for questionnaire page
    path("chat/", include("chat.urls")),  # path for instant chat pages
    path('messages/', include('user_messages.urls')),  # path for messages page
    path('profiles/', include('profiles.urls')),  # path for profiles page
    path('contact/', include('contact.urls')),
    path('notifications/', include('notificationapp.urls')),
]

if settings.DEBUG:  # Only serve media files in development mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
