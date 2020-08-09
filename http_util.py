import urllib.request
import os


def post(hex_list):
  url = 'http://39.101.201.108:5556/'
  headers = {
      'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
  }
  values = {
    'hex': hex_list
  }
  data = urllib.parse.urlencode(values).encode('utf-8')
  request = urllib.request.Request(url, data, headers)
  html = urllib.request.urlopen(request).read().decode('utf-8')
  print(html)