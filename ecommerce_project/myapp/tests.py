from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

"""
To run the tests here, run the command python manage.py test
Make sure all the method name starts with test_
"""


class ProductTestCases(TestCase):
    def test_get_all_products(self):
        # request_body = {
        #     'param1  ': 'param1value',
        #     'param2': 'param2value'
        # }
        client = APIClient()
        response = client.get(path='/products/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
