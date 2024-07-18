import json
import os
import base64
import time

from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
timer = time.perf_counter

def audio_to_text(audio_file):
    API_KEY = os.environ.get("API_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FORMAT = audio_file[-3:]
    CUID = '93918488'
    RATE = 16000
    DEV_PID = 80001
    ASR_URL = 'http://vop.baidu.com/pro_api'
    SCOPE = 'brain_enhanced_asr'

    TOKEN_URL = 'http://aip.baidubce.com/oauth/2.0/token'


    def fetch_token(API_KEY, SECRET_KEY):
        params = {'grant_type': 'client_credentials',
                'client_id': API_KEY,
                'client_secret': SECRET_KEY}
        post_data = urlencode(params)
        post_data = post_data.encode('utf-8')
        req = Request(TOKEN_URL, post_data)
        try:
            f = urlopen(req)
            result_str = f.read()
        except URLError as err:
            print('token http response http code : ' + str(err.code))
            result_str = err.read()
        result_str =  result_str.decode()
        result = json.loads(result_str)
        
        if ('access_token' in result.keys() and 'scope' in result.keys()):
            print(SCOPE)
            if SCOPE and (not SCOPE in result['scope'].split(' ')):  # SCOPE = False 忽略检查
                return None
            return result['access_token']
        else:
            return None

    token = fetch_token(API_KEY=API_KEY, SECRET_KEY=SECRET_KEY)

    speech_data = []
    with open(audio_file, 'rb') as speech_file:
        speech_data = speech_file.read()

    length = len(speech_data)
    if length == 0:
        return None
    speech = base64.b64encode(speech_data)
    speech = str(speech, 'utf-8')
    params = {'dev_pid': DEV_PID,
            'format': FORMAT,
            'rate': RATE,
            'token': token,
            'cuid': CUID,
            'channel': 1,
            'speech': speech,
            'len': length
            }
    post_data = json.dumps(params, sort_keys=False)
    req = Request(ASR_URL, post_data.encode('utf-8'))
    req.add_header('Content-Type', 'application/json')
    try:
        begin = timer()
        f = urlopen(req)
        result_str = f.read()
        print ("Request time cost %f" % (timer() - begin))
    except URLError as err:
        print('asr http response http code : ' + str(err.code))
        result_str = err.read()

    result_str = str(result_str, 'utf-8')
    return eval(result_str)['result'][0]

#print(audio_to_text('C:/Users/PC/Desktop/16k.wav'))