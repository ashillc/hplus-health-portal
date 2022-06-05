from django.db import models
from django.db.models import JSONField


class Profile(models.Model):
    """Model class to store profile information."""
    name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.TextField(max_length=100, blank=True)
    address = models.TextField(max_length=300, blank=True)
    member_since = models.DateField(null=True)
    picture = models.ImageField(upload_to='images', default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Appointments(models.Model):
    """Model class to store appointment information."""
    name = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(null=True)
    doctor = models.CharField(max_length=100, blank=True)
    medical_speciality = models.TextField(max_length=100, blank=True)
    branch_address = models.TextField(max_length=300, blank=True)
    viewed = models.BooleanField(default=False)
