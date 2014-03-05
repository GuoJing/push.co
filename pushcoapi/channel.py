# -*- coding: utf-8 -*-

'''
Push.co Channel
'''

import requests

from .consts import CHANNEL_URL


class Channel(object):

    def __init__(self, access_token):
        self.access_token = access_token

    def get(self):
        '''
        Get the list of channels for your app for a specific user
        all based on the Access Token. The whole idea is that
        you can present a list of channels
        specific for the user in the Push.co app.
        For example, you want to show a generic user generic channels
        but you want to show an admin user some extra channels.
        '''
        data = requests.get(CHANNEL_URL,
                            params=dict(access_token=self.access_token))
        return data.json()

    def post(self, channels):
        '''
        Assign a list of channels to your app for a specific user
        all based on the Access Token.
        The whole idea is that you can present a
        list of channels specific for the user in the Push.co app.
        You can go all out! For example
        you want to show a generic user generic channels
        but you want to show an admin user some extra channels.

        channels example

        [
            {
                'notification_type':'CHANNEL 1',
                'notification_type': {
                    'name' : 'CHANNEL 2',
                    'public' : false
                },
                'notification_type':'CHANNEL 3',
                ....
            }
        ]
        '''
        data = dict(access_token=self.access_token,
                    channels=channels)
        data = requests.post(CHANNEL_URL, data=data)
        return data.json()
