from rest_framework import viewsets
from .models import Profile, Appointments
from .serializers import ProfileSerializer, AppointmentsSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """Viewset to service the profile model."""
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """Overload the get_queryset method."""
        queryset = Profile.objects.all()
        filters = {}
        for key, value in self.request.query_params.items():
            filters[key] = value

        queryset = queryset.filter(**filters)

        return queryset


class AppointmentsViewSet(viewsets.ModelViewSet):
    """Viewset to service the appointment model."""
    serializer_class = AppointmentsSerializer

    def get_queryset(self):
        """Overload the get_queryset method."""
        queryset = Appointments.objects.all()
        filters = {}
        for key, value in self.request.query_params.items():
            filters[key] = value
        queryset = queryset.filter(**filters)

        return queryset
