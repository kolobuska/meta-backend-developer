from django.test import TestCase
from django.test import Client
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        item1 = Menu.objects.create(title = "IceCream", price = 80, inventory = 10)
        item2 = Menu.objects.create(title = "Tiramisu", price = 2000, inventory = 100)
    
    def test_getall(self):
        items = Menu.objects.all()
        test_client = Client()
        response = test_client.get('/restaurant/menu/')
        self.assertEqual(200, response.status_code)

        expected_response = '[{"title":"IceCream","price":"80.00","inventory":10},{"title":"Tiramisu","price":"2000.00","inventory":100}]'
        self.assertEqual(expected_response, response.content.decode('UTF-8'))
