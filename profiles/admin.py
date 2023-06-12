from django.contrib import admin

from .models import Profile
from .models import Rate
from .models import Recommendation_Model
# Register your models here.
admin.site.register(Profile)
admin.site.register(Rate)
admin.site.register(Recommendation_Model)

