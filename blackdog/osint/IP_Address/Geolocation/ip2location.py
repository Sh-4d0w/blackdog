import django
from django.middleware.csrf import CsrfViewMiddleware, get_token
from django.test import Client
import standalone
import os
standalone.run('dsa.settings') # replace with your settings module.

class Ip2Location:
    def __init__(self):
        self._url = "www.ip2location.com/"

    def test(self):
        import sys
        django.setup()
        csrf_client = Client(enforce_csrf_checks=True)


        # Retrieve the CSRF token first
        csrf_client.get(self._url)  # sets cookie
        #csrftoken = csrf_client.cookies['csrftoken']
        print(csrf_client)
        #login_data = dict(username=EMAIL, password=PASSWORD, csrfmiddlewaretoken=csrftoken.value, next='/')
        #r = csrf_client.post(URL, data=login_data, headers=dict(Referer=URL))
a= Ip2Location().test()