from http import client
from django.core.exceptions import ValidationError
from django.test import TestCase

# Create your tests here.
from base64 import encode
from django.test import TestCase
from selenium import webdriver
from .forms import HashForm
import hashlib
from .models import Hash
import time
# Create your tests here.

class FunctionalTestCase(TestCase):
    def setUp(self): # runs on start of test
        self.browser = webdriver.Chrome()

    def test_there_is_homepage(self):
        self.browser.get('http://www.localhost:8000')
        self.assertIn('Enter plane text.', self.browser.page_source)
    
    def test_hashofhello(self):
        self.browser.get('http://www.localhost:8000')
        text_field = self.browser.find_element('id', 'id_text')
        text_field.send_keys('hello')
        self.browser.find_element('name', 'submit').click()
        self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)

    def test_hash_ajax(self):
        self.browser.get('http://www.localhost:8000')
        text_field = self.browser.find_element('id', 'id_text')
        text_field.send_keys('hello')
        time.sleep(5)
        self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)

    def tearDown(self): # runs after the test has occured.
        self.browser.quit()

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

    def saveHash(self):
        hash  = Hash()
        hash.text = 'hello'
        hash.hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        hash.save()
        return hash

    def test_hash(self):
        hash = self.saveHash()
        grabbed_hash = Hash.objects.get(hash='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertEqual(grabbed_hash.hash, hash.hash)
    
    def test_hash_text(self):
        hash = self.saveHash()
        grabbed_hash = Hash.objects.get(hash='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertEqual(grabbed_hash.text, hash.text)
    
    def test_get_hash(self):
        self.saveHash()
        response = self.client.get('/hash/2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertContains(response, 'hello')

    def test_hash_validation(self):
        def badHash():
            hash = Hash()
            hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
            return hash.full_clean()
        self.assertRaises(ValidationError, badHash)