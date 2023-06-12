from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from project import settings
from project.settings import MEDIA_ROOT
from PIL import Image
from django.db.models.signals import post_save
from django.utils.text import slugify
from urllib.parse import urlparse
from django.db.models import Avg, Count
from django.utils.translation import gettext_lazy as _

from django.db.models import Avg

# محتاجة تعملى migrations و migrate
# Create your models here.


def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "profile/%s/%s" % (instance.id, extension)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{1}'.format(instance.user.id, filename)

    
class Profile(models.Model):
    # بتستدعى ال attribute دة
    ##
    image = models.ImageField(default='user.png', upload_to=image_upload)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    email = models.EmailField(max_length=30, default='none')
    phone_number = models.CharField(max_length=15, default='none')
    # age=models.CharField(max_length=15 ,default='none')
    city = models.CharField(max_length=30, default='none')
    gender = models.CharField(max_length=15, default='male')
    education = models.CharField(default='none', max_length=200)
    tecskill = models.CharField(default='none', max_length=200)
    softskill = models.CharField(default='none', max_length=200)
    language = models.CharField(default='none', max_length=200)
    experience = models.CharField(default='none', max_length=400)
    bio = models.TextField(default='none')
    dob = models.DateField(blank=True, null=True)
    cv = models.FileField(upload_to=user_directory_path,
                          max_length=40, default='none')
    file = models.FileField(upload_to=user_directory_path,
                            max_length=40, default='none')
    face=models.CharField(null=False,blank=False, max_length=200)
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.user)
    
    face_name = models.CharField(null=True, blank=True, max_length=200)

    def average_quality(self):
         review = Rate.objects.filter(RA_Other=self).aggregate(average=Avg('RAtingQuality'))
         avg = 0
         if review["average"] is not None:
             avg = float(review["average"])
         return avg
    def average_speed(self):
         review = Rate.objects.filter(RA_Other=self).aggregate(average=Avg('RAtingSpeed'))
         avg = 0
         if review["average"] is not None:
             avg = float(review["average"])
         return avg
    def average_moralistic(self):
         review = Rate.objects.filter(RA_Other=self).aggregate(average=Avg('RAtingMoralistic'))
         avg = 0
         if review["average"] is not None:
             avg = float(review["average"])
         return avg
    def count_review(self):
        reviews = Rate.objects.filter(RA_Other=self).aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt

    def save(self, *args, **kwargs):
        if self.face:
            parsed_url = urlparse(self.face)
            path = parsed_url.path
            if path.startswith('/'):
                path = path[1:]
            if path.endswith('/'):
                path = path[:-1]
            name = path.split('/')[-1]
            self.face_name = name
        super().save(*args, **kwargs)


    

    # def save(self):
        # super().save()

        # img = Image.open(self.image.path)

        # if img.height > 300 or img.width >300:
        # output_size = (300,300)
        # img.thumbnail(output_size)
        # img.save(self.image.path)
    


class Rate(models.Model):

    RAUser           = models.ForeignKey(User , on_delete=models.CASCADE , blank=True, null=True ,verbose_name=_("User"))
    RA_Other         = models.ForeignKey('Profile' , on_delete=models.CASCADE , blank=True, null=True ,verbose_name=_("Profile"))
    RAtingQuality    = models.IntegerField(default='0')
    RAtingSpeed      = models.IntegerField(default='0')
    RAtingMoralistic = models.IntegerField(default='0')
    RADescription    = models.TextField(max_length=10000 , blank=True, null=True )

    

    def __str__(self):
        return f"{self.RAUser} reviewed  {self.RA_Other}"


def create_profile(sender, **kwargs):
    if kwargs['created']:
        try:
            user_profile = Profile.objects.create(user=kwargs['instance'])
        except Exception as e:
            print(f"Error saving profile: {str(e)}")

post_save.connect(create_profile, sender=User)


class Recommendation_Model (models.Model):

    User         = models.ForeignKey(User , on_delete=models.CASCADE , blank=True, null=True)
    Search_Words = models.TextField(max_length=1000, null= True, blank= True)

    def __str__(self):
        return self.Search_Words 
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.User:
            search_words = Recommendation_Model.objects.filter(User=self.User).order_by('-id')

            if search_words.count() > 5:
                older_search_words = search_words[5:]
                for word in older_search_words:
                    word.delete()