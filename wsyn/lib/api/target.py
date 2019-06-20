# coding: utf-8
import urllib
import requests

class Target:
    def __init__(self, url):
        self.__target_url = url
        self.__response = None

    @property
    def url(self):
        return self.__target_url
    
    @property
    def response(self):
        __response = self.request(self.url)
        self.__response = __response
        return self.__response

    def request(self, url):
        _response = requests.get(url)
        response = Response(_response)
        return response

class Response:
    def __init__(self, response):
        self.__response = response

    @property
    def url(self):
        return self.__response.url

    @property
    def text(self):
        return self.__response.text