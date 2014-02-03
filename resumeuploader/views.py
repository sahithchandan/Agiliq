# Create your views here.
import os
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import http
import requests
import json


def login(request):
    if request.method == 'GET':
        url = "http://join.agiliq.com/oauth/authorize"
        login_url = "{}?client_id={}&redirect_uri={}".format(url, os.environ['CLIENT_ID'], os.environ['REDIRECT_URI'])
        data = {"login_url": login_url}
        return render_to_response('login.html',
                                  data,
                                  context_instance=RequestContext(request))
    else:
        return http.HttpResponse('Send GET Method')


def form(request):
    if request.method == 'GET':
        if request.GET.get('code'):
            code = request.GET['code']
            pay_load = {"client_id": os.environ['CLIENT_ID'],
                        "client_secret": os.environ['CLIENT_SECRET'],
                        "redirect_uri": os.environ['REDIRECT_URI'],
                        "code": code}
            url = "http://join.agiliq.com/oauth/access_token/"
            response = requests.post(url, data=pay_load)
            result = json.loads(response.text)
            if 'access_token' in result:
                access_token = result['access_token']
                post_url = "http://join.agiliq.com/api/resume/upload/?access_token={}".format(access_token)
                data = {"post_url": post_url}
                return render_to_response('form.html',
                                          data,
                                          context_instance=RequestContext(request))
            else:
                return http.HttpResponse('No access token.')
        else:
            return http.HttpResponse('Server Error. No "code" in request.')
    else:
        return http.HttpResponse('Send GET Method')