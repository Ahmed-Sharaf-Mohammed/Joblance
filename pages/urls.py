from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('feedback', views.send_message, name='feedback'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
