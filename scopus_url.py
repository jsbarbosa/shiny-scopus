# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:13:40 2016

@author: juan
"""

from my_api import *
import urllib.request as urllib2
import datetime
import requests
import json
import time

scopus_author_search_url = 'http://api.elsevier.com/content/search/scopus?'
headers = {'Accept':'application/json', 'X-ELS-APIKey': SCOPUS_API_KEY}
#search_query = 'query=AUTHFIRST(%s) AND AUTHLASTNAME(%s) AND SUBJAREA(%s)' % ('Ricardo', 'Bonilla', 'SOCI')

#search_query = 'query=AUTHFIRST(%s) AND AUTHLASTNAME(%s)' % ('Ricardo', 'Bonilla')
search_query = 'query=AU-ID(56196626500)&field=dc:identifier&count=10'#author_id=56196626500&view=metrics'#query=AUTHID(56196626500)&count=100'
#AU-ID(7004212771)"

# api_resource = "http://api.elsevier.com/content/search/author?apiKey=%s&" % (SCOPUS_API_KEY)

url = scopus_author_search_url+search_query
def request_until_succeed(url, headers):
    success = False
    while success is False:
        try: 
            response = requests.get(url, headers=headers)
            print(response.status_code)
            if response.status_code == 200:
                success = True
        except Exception as e:
            print(e)
            time.sleep(5)
            
            print("Error for URL %s: %s" % (url, datetime.datetime.now()))

    return response


# request with first searching page
#page_request = request_until_succeed(url, headers)
page_request = requests.get(url, headers=headers)
print(page_request.url)

# response to json
page = json.loads(page_request.content.decode("utf-8"))


#for item in page['search-results']['entry']:
#    print(json.dumps(item, indent=4, sort_keys=True))
nice = json.dumps(page, indent=4, sort_keys=True)
print(nice)
