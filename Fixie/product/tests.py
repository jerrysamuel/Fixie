from django.test import TestCase
from .models import products
#check for models in the db 
class productsModelTest(TestCase):
    def test_product_model_exists(self):
        product = products.objects.count()

        self.assertEqual(product, 0)

    def test_model_has_string_representation(self):
        product =products.objects.create(name= 'iphone 12', description ='jhgdsjgmfhj')

        self.assertEqual(str(product), product.name)