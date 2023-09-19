from django.test import TestCase

from ..models import *
from ..serializers import *

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title = 'IceCream', Price = 2.99, Inventory = 50)
        self.assertEqual(item.__str__(), "IceCream : 2.99")

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title = 'IceCream', Price = 2.99, Inventory = 50)
        Menu.objects.create(Title = 'Molten Cake', Price = 17.99, Inventory = 150)

    def test_getall(self):
        data = Menu.objects.all()
        serializedData = MenuSerializer(data, many = True).data
        self.assertEqual(len(serializedData), 2)