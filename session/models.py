from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    BlOOD_GROUP = (
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    GENRE_CHOICES = (
        ('Male', 'MALE'),
        ('Female', 'FEMALE'),
    )
    CATEGORY = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    blood_group = models.CharField(max_length=10, choices=BlOOD_GROUP)
    gender = models.CharField(max_length=50, choices=GENRE_CHOICES)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    nationality = models.CharField(max_length=30)
    religion = models.CharField(max_length=50)
    biodata = models.TextField()
    profession = models.CharField(max_length=50, choices=CATEGORY)
    image = models.ImageField(default='default.png',
                              upload_to='session/images')

    def __str__(self):
        return f'{self.user.username}Profiles'

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300 :
            output_size =(300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
