from django.shortcuts import redirect, render
from .models import Craftsmen ,Rating
from django.contrib import messages

# Create your views here.


def members(request):
    return render(request, 'features/members.html')


def craftsmen(request):

    craftsmen_list = Craftsmen.objects.all()
    top_rate = Craftsmen.get_top_rated_craftsmen()
    context = {'list': craftsmen_list,'top_rate':top_rate
               }
    return render(request, 'features/craftsmen.html', context)


def about_us(request):
    return render(request, 'features/AboutUs.html')


def career(request):
    return render(request, 'features/career.html')


def interview(request):
    return render(request, 'features/interview.html')

def craftsman_detail(request, craftsman_id):
    craftsman_details = Craftsmen.objects.get(id=craftsman_id)
    Rev =craftsman_details.average_review()
    rating_details = Rating.objects.filter(RACraftsmen=craftsman_details)
    context = {'craftsman_detail': craftsman_details ,'rating_details': rating_details , 'Rev':Rev}
    return render(request, 'features/craftsman_detail.html', context)



def submit_rating(request, craftsmanId):
    if request.method == 'POST':
        user = request.user
        craftsman = Craftsmen.objects.get(id=craftsmanId)
        rating_value = request.POST.get('rating')
        description = request.POST.get('description')
        existing_rating = Rating.objects.filter(RAUser=user, RACraftsmen=craftsman).first()
        if existing_rating:
            # An existing rating was found, update it with new values
            if rating_value is None and description == '':
                # Neither rating nor description is provided, inform the user to fill in one of the two fields
                messages.warning(request, "Please fill in either the rating or the description field.")
            else:
                existing_rating.RAting = rating_value
                existing_rating.RADescription = description
                existing_rating.save()
                messages.success(request, "The rating has been updated successfully.")
        else:
            # No rating exists for this user and craftsman, create and save a new Rating object
            if rating_value is None and description == '':
                # Neither rating nor description is provided, inform the user to fill in one of the two fields
                messages.warning(request, "Please fill in either the rating or the description field.")
            else:
                rating = Rating(RAUser=user, RACraftsmen=craftsman, RAting=rating_value, RADescription=description)
                rating.save()
                messages.success(request, "The evaluation of Craftsmen has been completed successfully.")
        return redirect('features:craftsman_detail', craftsman_id=craftsmanId)