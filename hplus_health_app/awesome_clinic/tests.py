from django.test import TestCase
from awesome_clinic.models import Profile, Appointments


class HealthAppTestCases(TestCase):
    """Test class for hplus health app."""
    def setUp(self) -> None:
        """Define the test client and other test variables."""
        self.profile = Profile.objects.create(
            name="test_name",
            phone="0821234560",
            email="test@gmail.com",
            address="1 test drive, test, 2090",
            member_since="2022-05-05"
        )

    def test_model_can_create_a_container(self) -> None:
        """Test the container model can create a container."""
        pass

# Create your tests here.
