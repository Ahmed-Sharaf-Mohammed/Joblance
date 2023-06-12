from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'job'
urlpatterns = [
    path('', views.jobs_list, name='job_list'),
    path('add', views.add_job, name='add_job'),
    path('your_jobs', views.your_jobs, name='your_jobs'),
    path('jobs/<int:job_id>/delete/', views.delete_job, name='delete_job'),
    path('<int:id>', views.edit_job, name='edit_job'),
    path('<str:slug>', views.job_details, name='job_details'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
