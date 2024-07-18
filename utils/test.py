import requests
import json
import base64
import os


def main():

    audio_file = 'C:/Users/PC/Desktop/test.m4a'
    with open(audio_file, 'rb') as f:
        audiodata = base64.b64encode(f.read()).decode()
    url = "https://vop.baidu.com/pro_api"
    
    payload = json.dumps({
        "format": "m4a",
        "rate": 16000,
        "channel": 1,
        "cuid": "OxRAEvhmVKZ24Xk3wXx9nalypcrQtHeB",
        "token": get_access_token(),
        "dev_pid": 80001,
        "len": len(audio_file),
        "speech": audiodata,
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    print(os.environ.get("API_KEY"))
    params = {"grant_type": "client_credentials", "client_id": os.environ.get("API_KEY"), "client_secret": os.environ.get("SECRET_KEY")}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    main()
