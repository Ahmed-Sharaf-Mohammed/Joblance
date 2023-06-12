from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

CURRENT_CITY = (
    ('Cairo', 'Cairo'),
    ('Giza', 'Giza'),
    ('ALexandria', 'ALexandria'),
    ('Ismailia', 'Ismailia'),
    ('Port Said', 'Port Said'),
    ('Suez', 'Suez'),
    ('Luxor', 'Luxor'),
    ('Mansoura', 'Mansoura'),
    ('El-Mahalla', 'El-Mahalla'),
    ('Tanta', 'Tanta'),
    ('Aswan', 'Aswan'),
    ('Asyut', 'Asyut'),
    ('Zagazig', 'Zagazig'),
    ('Damietta', 'Damietta'),
    ('Damanhur', 'Damanhur'),
    ('Minya', 'Minya'),
    ('Sohag', 'Sohag'),
    ('Qena', 'Qena'),
    ('Hurghada', 'Hurghada'),
    ('Banha', 'Banha'),
)

CURRENT_COUNTRY = (
    ('Egypt', 'Egypt'),
)


class Job(models.Model):
    owner = models.ForeignKey(
        User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=10000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    country = models.CharField(max_length=15, choices=CURRENT_COUNTRY)
    city = models.CharField(max_length=15, choices=CURRENT_CITY)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Apply(models.Model):
    job = models.ForeignKey(
        Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    webiste = models.URLField(blank=True)
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
