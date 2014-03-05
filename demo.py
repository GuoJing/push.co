# -*- coding: utf-8 -*-

'''
This is a simple demo how to use this lib
'''

api_key = ''
api_secret = ''
redirect_url = 'http://localhost:4000'

try:
    input = raw_input
except:
    pass


def auth():
    from pushcoapi.authorize import Authorize

    auth = Authorize(api_key, api_secret, redirect_url)

    url = auth.get_auth_url()
    print('1. Go to link below')
    print('2. Click Allow')
    print('3. Copy the authorization code.')
    print(url)
    code = input("Enter the authorization code here: ").strip()

    data = auth.get_access_token(code)

    print(data)

    access_token = data.get('access_token')

    data = auth.check_access_token(access_token)

    print(data)

    #data = auth.delete_access_token(access_token)

    #print data
    return access_token


def subscription(access_token):
    from pushcoapi.subscription import Subscription
    s = Subscription(access_token)
    print(s.gets())


def push():
    from pushcoapi.push import Push
    p = Push(api_key, api_secret)
    ret = p.push_message('Hello, this is a message from demo')
    print(ret)

    ret = p.push_web('Hello, this is a web', 'http://guojing.me')
    print(ret)

    ret = p.push_map('Hello, this is a map', '39.9026266648', '116.4012871818')
    print(ret)

if __name__ == '__main__':
    push()
