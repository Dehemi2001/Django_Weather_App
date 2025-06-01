from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from urllib.error import URLError

class WeatherViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def test_get_request_renders_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter city name")

    @patch('weather.views.urllib.request.urlopen')
    def test_post_valid_city(self, mock_urlopen):
        # Mock API response
        mock_response = b'''
        {
            "main": {"temp": 300.15, "pressure": 1012, "humidity": 80},
            "sys": {"country": "US"},
            "coord": {"lon": -122.08, "lat": 37.39},
            "weather": [{"icon": "01d", "description": "clear sky"}]
        }
        '''
        mock_urlopen.return_value.read.return_value = mock_response

        response = self.client.post(self.url, {'city': 'Mountain View'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "US")
        self.assertContains(response, "Clear sky")  # Capitalized
        self.assertContains(response, "27.0°C")  # 300.15K - 273.15 = 27.0°C

    @patch('weather.views.urllib.request.urlopen', side_effect=URLError("City not found"))
    def test_post_invalid_city(self, mock_urlopen):
        response = self.client.post(self.url, {'city': 'InvalidCity'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "City not found or invalid input. Please enter a valid city name.")