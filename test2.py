# -*- coding: utf-8 -*-

import json
import requests


def send_post(url, send_data, headers = {'content-type': 'application/json'}):
    """POST请求"""
    r = requests.post(url, data=send_data, headers=headers)

    return r
  
if __name__ == '__main__':  # pragma nocover
    urlstr = 'http://127.0.0.1:8089/test'
    #json_data = json.dumps(['http://localhost/imgareaselect/imgs/1.jpg','http://localhost/imgareaselect/imgs/2.jpg'])
    data={'passtime': '2015-02-24 12:23:34'}
    r = send_post(urlstr, json.dumps(data))
    print r.status_code
    print r.text
