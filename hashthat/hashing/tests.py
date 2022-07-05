from django.test import TestCase

# Create your tests here.
from base64 import encode
from django.test import TestCase
from selenium import webdriver
from .forms import HashForm
import hashlib
# Create your tests here.

# class FunctionalTestCase(TestCase):
#     def setUp(self): # runs on start of test
#         self.browser = webdriver.Chrome()

#     def test_there_is_homepage(self):
#         self.browser.get('http://www.localhost:8000')
#         self.assertIn('Enter plane text.', self.browser.page_source)
    
#     def test_hashofhello(self):
#         self.browser.get('http://www.localhost:8000')
#         text_field = self.browser.find_element_by_id('plane-test')
#         text_field.send_keys('hello')
#         self.browser.find_element_by_name('submit').click()
#         self.assertIn('2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824', self.browser.page_source)

#     def tearDown(self): # runs after the test has occured.
#         self.browser.quit()


class UnitTestCase(TestCase):
    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_hash_form(self):
        form = HashForm(data={'text':'hello'})
        self.assertTrue(form.is_valid())
    
    def test_hash(self):
        self.my_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.my_hash)