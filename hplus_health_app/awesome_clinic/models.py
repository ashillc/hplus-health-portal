from django.db import models


class Profile(models.Model):
    """Model class to store profile information."""

    name = models.CharField(max_length=30, blank=True)  # Name of client
    phone = models.CharField(max_length=30, blank=True)  # Phone of client
    email = models.TextField(max_length=100, blank=True)  # Email of client
    address = models.TextField(max_length=300, blank=True)  # Address of patient
    member_since = models.DateField(null=True)  # Date client started being a member of awesome clinic
    picture = models.ImageField(upload_to="images", default=None, blank=True, null=True)  # Picture of client


class Appointments(models.Model):
    """Model class to store appointment information."""

    name = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)  # Relation to client
    date = models.DateTimeField(null=True)  # Date of Appointment
    doctor = models.CharField(max_length=100, blank=True)  # Name of doctor
    medical_speciality = models.TextField(max_length=100, blank=True)  # Medical Speciality of doctor
    branch_address = models.TextField(max_length=300, blank=True)  # Address of practice
    viewed = models.BooleanField(default=False)  # Has this appointment been viewed already?
