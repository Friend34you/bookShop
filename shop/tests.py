import unittest

from django.test import LiveServerTestCase
import time
from django.test import TestCase
from django.urls import reverse
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class CustomerListTestCase(LiveServerTestCase):

    def setUp(self):
        self.client.login(username="root", password="00000")
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        self.selenium.get('http://127.0.0.1:8000/')
        super(CustomerListTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(CustomerListTestCase, self).tearDown()

    def test_successful_login(self, username="vova", password="88005553535v"):
        self.selenium.get('http://127.0.0.1:8000/accounts/login/')
        username_el = self.selenium.find_element(By.NAME, "username")
        time.sleep(1)
        username_el.send_keys(username)
        password_el = self.selenium.find_element(By.NAME, "password")
        time.sleep(1)
        password_el.send_keys(password)
        submit = self.selenium.find_element(By.ID, 'login')
        time.sleep(1)
        submit.send_keys(Keys.RETURN)
        time.sleep(1)
        assert self.selenium.current_url == "http://127.0.0.1:8000/"

    def test_unsuccessful_login(self, username="admin1", password="12345678910"):
        self.selenium.get('http://127.0.0.1:8000/accounts/login/')
        username_el = self.selenium.find_element(By.NAME, "username")
        time.sleep(1)
        username_el.send_keys(username)
        password_el = self.selenium.find_element(By.NAME, "password")
        time.sleep(1)
        password_el.send_keys(password)
        submit = self.selenium.find_element(By.ID, 'login')
        submit.send_keys(Keys.RETURN)
        time.sleep(1)
        assert self.selenium.current_url == "http://127.0.0.1:8000/accounts/login/"
