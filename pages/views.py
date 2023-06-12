from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from job.models import Job
from features.models import Craftsmen
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    craftsmen = Craftsmen.objects.all()[:6]
    top_rate = Craftsmen.get_top_rated_craftsmen()[:6]
    jobs_list = Job.objects.all()[:6]
    context = {'jobs': jobs_list,
               'workers': top_rate,
               }
    return render(request, 'pages/index.html', context)


def home(request):
    return render(request, 'pages/home.html')


@login_required()
def send_message(request):
    myinfo = Info.objects.first()
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            email,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )

    return render(request, 'pages/feedback.html', {'myinfo': myinfo})
