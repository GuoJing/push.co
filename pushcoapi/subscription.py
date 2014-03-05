# -*- coding: utf-8 -*-

'''
Push.co Subscription
'''

import requests

from .consts import SUBSCRIPTION_URL, SUBSCRIPTION_LINK_URL


class Subscription(object):

    def __init__(self, access_token):
        self.access_token = access_token

    def gets(self):
        '''
        Get all subscriptions for the user bound to the send Access Token.
        Since Access Tokens are also bound to your Push app
        you'll only see the subscriptions for your Push app.
        '''
        data = requests.get(SUBSCRIPTION_URL,
                            params=dict(access_token=self.access_token))
        return data.json()

    def add(self, name, api_key, notification_type=''):
        '''
        You can use this method to subscribe people to your Push app.
        You'll need an Access Token so we can identify the user and Push app.
        '''
        data = dict(access_token=self.access_token,
                    name=name,
                    api_key=api_key,
                    notification_type=notification_type)
        data = requests.post(SUBSCRIPTION_URL, data=data)
        return data.json()

    def delete(self, api_secret, notification_type=''):
        '''
        So you want to unsubscribe user from your Push app?
        This works the same as making a subscription.
        You'll need an Access Token.
        Because the Access Token already points to the API key,
        you don't need to include it.
        '''
        data = dict(access_token=self.access_token,
                    api_secret=api_secret,
                    notification_type=notification_type)
        data = requests.delete(SUBSCRIPTION_URL, data=data)
        return data.json()

    def get_link(self, api_key, api_secret, name, notification_type=''):
        '''
        This method generates special links (URL schemes) that allows users to
        subscribe really easily. There's a catch. The user needs to open this
        link on the iPhone with the Push.co app installed.
        It will open the Push.co app and make the subscription on the fly.
        '''
        data = dict(api_key=api_key,
                    api_secret=api_secret,
                    name=name,
                    notification_type=notification_type)
        data = requests.post(SUBSCRIPTION_LINK_URL, data=data)
        return data.json()
