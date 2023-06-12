"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('jobs/', include('job.urls', namespace='jobs')),
    path('', include('pages.urls', namespace='pages')),
    path('profile/', include('profiles.urls', namespace='profiles')),
    path('registration/', include('registration.urls', namespace='registration')),
    path('features/', include('features.urls', namespace='features')),
    # هنا انا استخدمت كل ال methods الداخلية فى ال django
    # الجاهزة اللى موجودة فى ال registration
    # اللى هى كتبناها فى فايل txt

    path("accounts/", include("django.contrib.auth.urls")),
    # عشان اوصل لمكان ال template
    # واعرف اساميهم امشى على نفس المسار اللى مكتوب
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
