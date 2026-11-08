import unittest
from app.app import app


class TestWorkdayPortal(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_dashboard(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.client.get("/profile")
        self.assertEqual(response.status_code, 200)

    def test_attendance(self):
        response = self.client.get("/attendance")
        self.assertEqual(response.status_code, 200)

    def test_leave(self):
        response = self.client.get("/leave")
        self.assertEqual(response.status_code, 200)

    def test_requests(self):
        response = self.client.get("/requests")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
