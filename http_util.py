import http.client
import json

def post_json(server_path,url,p_data):
  json_str = json.dumps(p_data)
  headers = {"Content-type": "application/json","Accept": "*/*"}
  path = server_path.split(':')
  conn = http.client.HTTPConnection(path[0],int(path[1]))
  conn.request('POST', url, json_str, headers)
  response = conn.getresponse()
  #print(response.status, response.reason)
  data = response.read().decode('utf-8')
  print(data)
  conn.close()

# def get_json:
#   json_str = json.dumps(p_data)
#   headers = {"Content-type": "application/json","Accept": "*/*"}
#   conn = http.client.HTTPConnection('39.101.201.108',9500)
#   conn.request('POST', url, json_str, headers)
#   response = conn.getresponse()
#   #print(response.status, response.reason)
#   data = response.read().decode('utf-8')
#   print(data)
#   conn.close()