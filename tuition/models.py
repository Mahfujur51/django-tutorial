from django.forms import ChoiceField
import django.utils.timezone
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from multiselectfield import MultiSelectField
from PIL import Image

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Class_in(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    CATEGORY = (('Teacher', 'Teacher'), ('Student', 'Student'))
    MY_CHOICES = (('Bangla', 'Bangla'),
                  ('English', 'English'),
                  ('Urdu', 'Urdu'),
                  ('Arabic', 'Arabic'),
                  ('Hindi', 'Hindi'))
   
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, default=title)
    email = models.EmailField()
    salary = models.IntegerField()
    details = models.TextField()
    availabe = models.BooleanField(default=True)
    category = models.CharField(max_length=100, choices=CATEGORY)
    created_at = models.DateTimeField(default=now)
    image = models.ImageField(default='default.jpg',
                              upload_to='tuition/images')
    medium = MultiSelectField(
        choices=MY_CHOICES, max_choices=3, max_length=100, default='Bangla')
    subject = models.ManyToManyField(Subject, related_name='subject_set')
    class_in = models.ManyToManyField(Class_in, related_name='class_set')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.title
    
    def get_subject_list(self):
        sub = self.subject.all()
        subjects=""
        for s in sub:
            subjects=subjects+str(s.name)+","
        return subjects
    def ProperCase(self):
        return self.title.title()
    def details_short(self):
        details_word=self.details.split(' ')
        if len(details_word)>10:
            return ' '.join(details_word[0:10])+"...."
        else:
            self.details
        
