from .models import Profile, Appointments
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer used for converting model information to json data."""
    class Meta:
        """Fields to return from the profile models."""
        model = Profile
        fields = "__all__"


class AppointmentsSerializer(serializers.ModelSerializer):
    """Profile serializer used for converting model information to json data."""
    class Meta:
        """Fields to return from the appointment models."""
        model = Appointments
        fields = "__all__"
