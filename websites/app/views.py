# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
    print "***START Power Card Introduction PAGE***"
    # try:
    ip =  get_client_ip(request)
    print 'ipppp ', ip

    from django.contrib.gis.geoip2 import GeoIP2
    g = GeoIP2()
    geo = g.country(str(ip))
    print 'geo ', geo

    from phonenumbers.phonenumberutil import country_code_for_region
    phone_code = country_code_for_region(geo['country_code'])
    print 'phone_code ', phone_code
    return render(request, 'websites/home.html')
    # except Exception, e:
    #     print "Error: ", e
    #     raise Exception( "ERROR : Internal Server Error .Please contact administrator.")


