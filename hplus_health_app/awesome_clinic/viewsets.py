from rest_framework import viewsets
from .models import Profile, Appointments
from .serializers import ProfileSerializer, AppointmentsSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class AppointmentsViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentsSerializer
