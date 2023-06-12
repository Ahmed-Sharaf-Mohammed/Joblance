from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'registration'
urlpatterns = [
    path('signin', views.LoginPage, name='signin'),
    path('signup', views.SignupPage, name='signup'),
    path('logout/', views.LogoutPage, name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
