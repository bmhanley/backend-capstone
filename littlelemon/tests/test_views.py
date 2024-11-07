from django.test import TestCase
from rest_framework.response import Response
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setup(self):
        MenuItem.objects.create(title="Caesar Salad", price=7.50, inventory=25)
        MenuItem.objects.create(title="Fish & Chips", price=12.99, inventory=20)
        MenuItem.objects.create(title="Bread Pudding", price=4.95, inventory=14)
        
    def test_getall(self):
        self.setup()
        items = MenuItem.objects.all()
        
        for item in items:
            serial = MenuItemSerializer(item)
            response = Response(serial.data)
            self.assertEqual(serial.data, response.data)