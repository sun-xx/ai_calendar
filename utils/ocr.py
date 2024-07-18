import os
import requests
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
import time
import json
timer = time.perf_counter
import base64

def fetch_token():
    API_KEY = os.environ.get("API_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    TOKEN_URL = 'http://aip.baidubce.com/oauth/2.0/token'
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    post_data = post_data.encode( 'utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req)
        result_str = f.read()
    except URLError as err:
        print('token http response http code : ' + str(err.code))
        result_str = err.read()
    
    result_str =  result_str.decode()

    result = json.loads(result_str)
    if 'access_token' in result.keys(): 
        return result['access_token']
    else:
        raise None

def ocr(image_path):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    f = open(image_path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    access_token = os.environ.get("ACCESS_TOKEN") # Set your own access token in your environment variables.
    request_url = request_url + "?access_token=" + fetch_token()
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        data = response.json()
        data = data["words_result"]
        s = ''
        for i in data:
            s += i["words"]

        return s
    else:
        return None
