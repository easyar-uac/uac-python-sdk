import requests
import sys
import time
import hashlib
import json

def get_sign(key, secret, params, key_name='apiKey'):
    if not isinstance(params, dict):
        return False
    params[key_name] = key
    params['timestamp'] = int(time.time() * 1000)
    params_str = ''.join(['%s%s' % (key, params[key]) for key in sorted(params.keys())]) + secret
    return hashlib.sha256(params_str.encode("utf8")).hexdigest()

if __name__ == '__main__':

    """  YOUR APIKey and APISecret here  """
    api_key = "<YOUR-API-KEY>"
    api_secret = "<YOUR-API-SECRET>"

    host = 'https://uac.easyar.com/token/v2'
    req_header = { 'Content-Type' : 'application/json; charset=UTF-8' }

    req_body = { "apiKey": api_key, "expires": 3600 }
    req_body ["signature"] = get_sign(api_key, api_secret, req_body)
    print(json.dumps(req_body) )

    response = requests.post(host, headers=req_header, data=json.dumps(req_body) )
    print(response.json())