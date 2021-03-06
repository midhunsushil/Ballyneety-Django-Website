"""ballyneety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', views.index, name="index"),
    path('about_us/', views.about_us, name="about_us"),
    path('mares/', views.mares, name="mares"),
    path('stallions/', views.stallions, name="stallions"),
    path('progeny/', views.progeny, name="progeny"),
    path('for_sale/', views.for_sale, name="for_sale"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('manage-2235/', include('manage_content.urls'), name="manage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Delete this during production
