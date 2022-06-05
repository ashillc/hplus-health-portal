from django.test import TestCase, Client
from awesome_clinic.models import Profile, Appointments
import json


class HealthAppTestCases(TestCase):
    """Test class for hplus health app."""

    def setUp(self) -> None:
        """Create database test entries."""

        self.profile = Profile.objects.create(
            name="test_name",
            phone="0821234560",
            email="test@gmail.com",
            address="1 test drive, test, 2090",
            member_since="2022-05-05",
        )

        self.profile2 = Profile.objects.create(
            name="test_name_2",
            phone="0224567890",
            email="test2@gmail.com",
            address="1 test2 drive, test2, 2090",
            member_since="2021-06-06",
        )

        self.appointment = Appointments.objects.create(
            date="2022-05-05T00:00:00",
            doctor="Dr A Smit",
            medical_speciality="Urology",
            branch_address="1 test drive, test, 2090",
            viewed=False,
            name=self.profile,
        )

        self.client = Client()

    def test_get_all_profile(self) -> None:
        """Test all profiles can be retrieved."""
        expected_response = [
            {
                "id": self.profile.pk,
                "name": "test_name",
                "phone": "0821234560",
                "email": "test@gmail.com",
                "address": "1 test drive, test, 2090",
                "member_since": "2022-05-05",
                "picture": None,
            },
            {
                "id": self.profile2.pk,
                "name": "test_name_2",
                "phone": "0224567890",
                "email": "test2@gmail.com",
                "address": "1 test2 drive, test2, 2090",
                "member_since": "2021-06-06",
                "picture": None,
            },
        ]

        actual_response = json.loads(self.client.get("/profile/").content)
        self.assertEqual(expected_response, actual_response)

    def test_get_single_profile_with_response(self) -> None:
        """Test a single profile can be retrieved."""
        expected_response = {
            "id": self.profile.pk,
            "name": "test_name",
            "phone": "0821234560",
            "email": "test@gmail.com",
            "address": "1 test drive, test, 2090",
            "member_since": "2022-05-05",
            "picture": None,
        }

        actual_response = json.loads(self.client.get(f"/profile/{self.profile.pk}/").content)

        self.assertEqual(expected_response, actual_response)

    def test_get_single_profile_with_filter_with_response(self) -> None:
        """Test a profile can be filtered."""
        expected_response = [
            {
                "id": self.profile2.pk,
                "name": "test_name_2",
                "phone": "0224567890",
                "email": "test2@gmail.com",
                "address": "1 test2 drive, test2, 2090",
                "member_since": "2021-06-06",
                "picture": None,
            }
        ]

        actual_response = json.loads(self.client.get("/profile/?name=test_name_2").content)

        self.assertEqual(expected_response, actual_response)

    def test_get_appointments(self) -> None:
        """Test an appointment can be retrieved."""
        expected_response = [
            {
                "id": self.appointment.pk,
                "date": "2022-05-05T00:00:00Z",
                "doctor": "Dr A Smit",
                "medical_speciality": "Urology",
                "branch_address": "1 test drive, test, 2090",
                "viewed": False,
                "name": self.profile.pk,
            }
        ]

        actual_response = json.loads(self.client.get("/appointment/").content)

        self.assertEqual(expected_response, actual_response)

    def test_patch_appointment(self) -> None:
        """Test an appointment can be modified."""
        expected_response = {
            "id": self.appointment.pk,
            "date": "2022-05-05T00:00:00Z",
            "doctor": "Dr B Jerry",
            "medical_speciality": "Urology",
            "branch_address": "1 test drive, test, 2090",
            "viewed": False,
            "name": self.profile.pk,
        }

        payload = {"doctor": "Dr B Jerry"}

        actual_response = json.loads(
            self.client.patch(
                f"/appointment/{self.appointment.pk}/", data=payload, content_type="application/json"
            ).content
        )

        self.assertEqual(expected_response, actual_response)

    def test_get_appointment_with_filter_with_response(self) -> None:
        """Test a profile can be filtered."""
        expected_response = [{
            "id": self.appointment.pk,
            "date": "2022-05-05T00:00:00Z",
            "doctor": "Dr A Smit",
            "medical_speciality": "Urology",
            "branch_address": "1 test drive, test, 2090",
            "viewed": False,
            "name": self.profile.pk,
        }]

        actual_response = json.loads(self.client.get("/appointment/?doctor=Dr A Smit").content)
        self.assertEqual(expected_response, actual_response)

    def test_delete_appointment(self) -> None:
        """Test an appointment can be delete."""

        self.client.delete(f"/appointment/{self.appointment.pk}/")

        actual_response = json.loads(self.client.get("/appointment/").content)

        self.assertEqual([], actual_response)

