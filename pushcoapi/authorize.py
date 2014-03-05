# -*- coding: utf-8 -*-

'''
Push.co Authorize
'''

import requests

from .consts import AUTHORIZE_URL, AUTHORIZE_ACCESS_TOKEN_URL


class Authorize(object):

    def __init__(self, api_key, api_secret, redirect_uri):
        self.api_key = api_key
        self.api_secret = api_secret
        self.redirect_uri = redirect_uri

    def get_auth_url(self):
        '''
        Request an Authorization code.
        The method will redirect the user to aPush.co login(if not logged in).
        After succesfully logging in, Push.co will redirect
        you back to the supplied redirect_uri
        with the Authorization code attached in the query string.
        Use it to get an Access Token.
        '''
        return '%s?api_key=%s&redirect_uri=%s' % (AUTHORIZE_URL,
                                                  self.api_key,
                                                  self.redirect_uri)

    def get_access_token(self, code, grant_type='authorization_code'):
        '''
        Request an Access Token with an Authorization code.
        For your convenience, the Access Token will not expire.
        code         -> code get by callback url
        grant_type   -> just set this value to `authorization_code`
        '''
        data = dict(code=code,
                    grant_type=grant_type,
                    api_key=self.api_key,
                    api_secret=self.api_secret,
                    redirect_uri=self.redirect_uri)
        data = requests.post(AUTHORIZE_ACCESS_TOKEN_URL, data=data)
        return data.json()

    def check_access_token(self, access_token):
        '''
        This method checks if the given Access Token is valid.
        When you do make request involving Access Tokens,
        you should always verify.
        '''
        body = requests.get(AUTHORIZE_ACCESS_TOKEN_URL,
                            params=dict(access_token=access_token))
        return body.json()

    def delete_access_token(self, access_token):
        url = AUTHORIZE_ACCESS_TOKEN_URL
        body = requests.delete(url, data=dict(access_token=access_token))
        return body.json()
