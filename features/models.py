from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from project import settings
from project.settings import MEDIA_ROOT
from PIL import Image
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from django.urls import reverse

def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "craftsmen/%s/%s" % (instance.id, extension)


class Craftsmen(models.Model):

     image = models.ImageField(default='user.png', upload_to=image_upload)
     name = models.CharField(max_length=30, default='none')
     slug = models.SlugField(null=True, blank=True)
     phone_number = models.IntegerField(default='none')
     profession = models.CharField(max_length=30, default='none')
     address = models.CharField(max_length=50, default='none')
     working_hours = models.CharField(max_length=50, default='none')
     description = models.TextField(max_length=10000)

     def __str__(self):
         return str(self.name)

     def get_absolute_url(self):
         return reverse('craftsman_detail', kwargs={'slug': self.slug})

     def average_review(self):
         review = Rating.objects.filter(RACraftsmen=self).aggregate(average=Avg('RAting'))
         avg = 0
         if review["average"] is not None:
             avg = float(review["average"])
         return avg

     def count_review(self):
         reviews = Rating.objects.filter(RACraftsmen=self).aggregate(count=Count('id'))
         cnt = 0
         if reviews["count"] is not None:
             cnt = int(reviews["count"])
         return cnt
     def get_top_rated_craftsmen():
        top_craftsmen = Craftsmen.objects.annotate(avg_rating=Avg('rating__RAting')).order_by('-avg_rating')[:9]
        return top_craftsmen
     
    
    
class Rating(models.Model):

    RAUser = models.ForeignKey(User , on_delete=models.CASCADE , blank=True, null=True ,verbose_name=_("User "))
    RACraftsmen = models.ForeignKey('Craftsmen' , on_delete=models.CASCADE , blank=True, null=True ,verbose_name=_("Craftsmen "))
    RAting = models.IntegerField(default='0')
    RADescription = models.TextField(max_length=10000 , blank=True, null=True )

    

    def __str__(self):
        return f"{self.RAUser} reviewed  {self.RACraftsmen}"

