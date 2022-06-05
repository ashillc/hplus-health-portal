from .models import Profile, Appointments
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = "__all__"
