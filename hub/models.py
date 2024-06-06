"""Models for bahk hub."""
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import constraints
from PIL import Image
from PIL import ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Church(models.Model):
    """Model for a church."""
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Fast(models.Model):
    """Model for a fast."""
    name = models.CharField(max_length=128)
    church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name="fasts")
    description = models.TextField(null=True, blank=True)
    culmination_feast = models.CharField(max_length=128, null=True, blank=True)
    culmination_feast_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='fast_images/', null=True, blank=True)
    # 2048 chars is the maximum URL length on Google Chrome
    url = models.URLField(verbose_name="Link to learn more", null=True, blank=True, max_length=2048,
                          help_text="URL to a link to learn more--must include protocol (e.g. https://)")

    class Meta:
        constraints = [
            constraints.UniqueConstraint(fields=["name", "church"], name="unique_name_church"),
            constraints.UniqueConstraint(fields=["culmination_feast_date", "church"], name="unique_feast_date_church"),
        ]

    def __str__(self):
        return f"{self.name} of the {self.church.name}"


class Profile(models.Model):
    """Model for a user profile.
    
    Based on https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    church = models.ForeignKey(Church, null=True, blank=True, on_delete=models.SET_NULL, related_name="profiles")
    fasts = models.ManyToManyField(Fast, related_name="profiles")
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True) 
    profile_image = models.ImageField(upload_to='profile_images/originals/')
    

    def __str__(self):
        return self.user.username


class Day(models.Model):
    """Model for a day in time."""
    date = models.DateField(unique=True)
    fasts = models.ManyToManyField(Fast, related_name="days")

    def __str__(self):
        return self.date.strftime("%B-%d-%Y")
