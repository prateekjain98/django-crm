from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    
    def test_status_code(self):
        response = self.client.get(reverse("home-page"))
        self.assertEqual(response.status_code, 200)
        
        #print(response.content)