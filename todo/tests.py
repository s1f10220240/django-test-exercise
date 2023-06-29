from django.test import TestCase

# Create your tests here.
class SampleTestCase(TestCase):
    def testsample1(self):
        self.assertEqual(1 + 2, 3)