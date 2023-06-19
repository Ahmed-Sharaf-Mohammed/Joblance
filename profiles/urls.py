from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from project.settings import MEDIA_ROOT
from . import views

from profiles.views import ChangePasswordView


app_name = 'profiles'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edite/', views.edite, name='edite'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    path('others/', views.others, name='others'),
    path('trans/', views.trans, name='trans'),
    path('<int:id>', views.other, name='other'),
    path('<int:rateid>/', views.submit_rating, name='submit_rating'),

    path('recommendations/', views.Recommendation_view, name='Recommendation_view'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
