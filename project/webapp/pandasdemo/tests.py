from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# from htmltext import find_text, format_html, gettext
from .models import*
import pandas as pd

class ViewsTestCase(TestCase):


    def test_loading_1(self):
        response = self.client.get('Dangy')
        self.assertEqual(response.status_code, 404)

    def test_loading_2(self):
        url1 = reverse('osnova')
        response = self.client.get(url1)
        self.assertEqual(response.status_code, 200)

    def test_loading_3(self):
        url1 = reverse('schema')
        response = self.client.get(url1)
        self.assertEqual(response.status_code, 200)

    def test_loading_4(self):
        response = self.client.get('https:django/anything')
        self.assertNotEqual(response, '<HttpResponseNotFound status_code=404, "text/html; charset=utf-8">')

    def test_loading_5(self):
        url1 = reverse('swagger-ui')
        response = self.client.get(url1)
        self.assertEqual(response.status_code, 200)



class ApiTest(APITestCase):
    def test_response_fine_1(self):
        url = reverse('api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_response_fine_2(self):
        url = reverse('api')
        response = self.client.get(url)
        self.assertEqual(response.data, {'Unnamed: 0': {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6},
'id': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7}, 'id_order': {0: 1, 1: 2, 2: 1, 3: 3, 4: 5, 5: 5, 6: 7},
'client_name': {0: 'Marshal', 1: 'Karl', 2: 'Marshal', 3: 'Maria', 4: 'Gabriel', 5: 'Gabriel', 6: 'Tanya'},
'client_surname': {0: 'Bugachev', 1: 'Golovko', 2: 'Bugachev', 3: 'Koval', 4: 'Agrest', 5: 'Agrest', 6: 'Chen'},
'order_date': {0: '03.11.2022', 1: '15.05.2022', 2: '03.11.2022', 3: '27.09.2022', 4: '04.08.2022', 5: '04.08.2022',
6: '11.12.2022'}, 'price': {0: 3500, 1: 6450, 2: 3500, 3: 10000, 4: 12000, 5: 12000, 6: 7800},
'del': {'Unnamed: 0': {0: 0, 1: 1, 2: 3, 3: 4, 4: 6}, 'id': {0: 1, 1: 2, 2: 4, 3: 5, 4: 7},
'id_order': {0: 1, 1: 2, 2: 3, 3: 5, 4: 7},
'client_name': {0: 'Marshal', 1: 'Karl', 2: 'Maria', 3: 'Gabriel', 4: 'Tanya'},
'client_surname': {0: 'Bugachev', 1: 'Golovko', 2: 'Koval', 3: 'Agrest', 4: 'Chen'}, 'order_date': {
0: '03.11.2022', 1: '15.05.2022', 2: '27.09.2022', 3: '04.08.2022', 4: '11.12.2022'},
'price': {0: 3500, 1: 6450, 2: 10000, 3: 12000, 4: 7800}}})

    def test_response_fine_3(self):
        url = reverse('api')
        response = self.client.get(url)
        self.assertNotEqual(response.data, {'Unnamed: 0': {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6},
'id': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7}, 'id_order': {0: 1, 1: 2, 2: 1, 3: 3, 4: 5, 5: 5, 6: 7},
'client_name': {0: 'Marshal', 1: 'Karl', 2: 'Zhukov', 3: 'Maria', 4: 'Gabriel', 5: 'Gabriel', 6: 'Tanya'},
'client_surname': {0: 'Bugachev', 1: 'Golovko', 2: 'Bugachev', 3: 'Koval', 4: 'Agrest', 5: 'Agrest', 6: 'Chen'},
'order_date': {0: '03.11.2022', 1: '15.05.2022', 2: '03.11.2022', 3: '27.09.2022', 4: '04.08.2022', 5: '04.08.2022',
6: '11.12.2022'}, 'price': {0: 3500, 1: 6450, 2: 3500, 3: 10000, 4: 12000, 5: 12000, 6: 7800},
'del': {'Unnamed: 0': {0: 0, 1: 1, 2: 3, 3: 4, 4: 6}, 'id': {0: 1, 1: 2, 2: 4, 3: 5, 4: 7},
'id_order': {0: 1, 1: 2, 2: 3, 3: 5, 4: 7},
'client_name': {0: 'Marshal', 1: 'Karl', 2: 'Maria', 3: 'Gabriel', 4: 'Tanya'},
'client_surname': {0: 'Bugachev', 1: 'Golovko', 2: 'Koval', 3: 'Agrest', 4: 'Chen'}, 'order_date': {
0: '03.11.2022', 1: '15.05.2022', 2: '27.09.2022', 3: '04.08.2022', 4: '11.12.2022'},
'price': {0: 3500, 1: 6450, 2: 10000, 3: 12000, 4: 7800}}})


    def test_response_fine_4(self):
        url = reverse('api')
        response = self.client.get(url)
        self.assertNotEqual(response.data, {'Unnamed: 0': {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6},
'id': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7}, 'id_order': {0: 1, 1: 2, 2: 1, 3: 3, 4: 5, 5: 5, 6: 7},
'client_name': {0: 'Marshal', 1: 'Karl', 2: 'Marshal', 3: 'Maria', 4: 'Gabriel', 5: 'Gabriel', 6: 'Tanya'},
'client_surname': {0: 'Bugachev', 1: 'Golovko', 2: 'Bugachev', 3: 'Koval', 4: 'Agrest', 5: 'Agrest', 6: 'Chen'},
'order_date': {0: '03.11.2022', 1: '15.05.2022', 2: '03.11.2022', 3: '27.09.2022', 4: '04.08.2022', 5: '04.08.2022',
6: '11.12.2022'}, 'price': {0: 3500, 1: 6450, 2: 3500, 3: 10000, 4: 12000, 5: 12000, 6: 10000000},
'del': {'Unnamed: 0': {0: 0, 1: 1, 2: 3, 3: 4, 4: 6}, 'id': {0: 1, 1: 2, 2: 4, 3: 5, 4: 7},
'id_order': {0: 1, 1: 2, 2: 3, 3: 5, 4: 7},
'client_name': {0: 'Marshal', 1: 'Karl', 2: 'Maria', 3: 'Gabriel', 4: 'Tanya'},
'client_surname': {0: 'Bugachev', 1: 'Golovko', 2: 'Koval', 3: 'Agrest', 4: 'Chen'}, 'order_date': {
0: '03.11.2022', 1: '15.05.2022', 2: '27.09.2022', 3: '04.08.2022', 4: '11.12.2022'},
'price': {0: 3500, 1: 6450, 2: 10000, 3: 12000, 4: 7800}}})


    def test_response_fine_5(self):
        url = reverse('api')
        response = self.client.get(url)
        self.assertNotEqual(response.data, {'Unnamed: 0': {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6},
'id': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7}, 'id_order': {0: 1, 1: 2, 2: 1, 3: 3, 4: 5, 5: 5, 6: 7},
'client_name': {0: 'Marshal', 1: 'Karl', 2: 'Marshal', 3: 'Maria', 4: 'Gabriel', 5: 'Gabriel', 6: 'Tanya'},
'client_surname': {0: 'Bugachev', 1: 'Golovko', 2: 'Bugachev', 3: 'Koval', 4: 'Agrest', 5: 'Agrest', 6: 'Chen'},
'order_date': {0: '03.11.2022', 1: '15.05.2022', 2: '03.11.2022', 3: '27.09.2022', 4: '04.08.2022', 5: '04.08.2022',
6: '11.12.2022'}, 'price': {0: 3500, 1: 6450, 2: 3500, 3: 10000, 4: 12000, 5: 12000, 6: 7800},
'del': {'Unnamed: 0': {0: 0, 1: 1, 2: 3, 3: 4, 4: 6}, 'id': {0: 1, 1: 2, 2: 4, 3: 5, 4: 7},
'id_order': {0: 1, 1: 2, 2: 3, 3: 5, 4: 7},
'client_name': {0: 'Marshal', 1: 'Karl', 2: 'Maria', 3: 'Gabriel', 4: 'Tanya'},
'client_surname': {0: 'Bugachev', 1: 'Golovko', 2: 'Koval', 3: 'Agrest', 4: 'Chen'}, 'order_date': {
0: '03.11.2022', 1: '15.05.2022', 2: '', 3: '', 4: ''},
'price': {0: 3500, 1: 6450, 2: 10000, 3: 12000, 4: 7800}}})




