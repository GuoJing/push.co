# -*- coding: utf-8 -*-

'''
Push.co Push
'''

import requests

from .consts import PUSH_URL


class Push(object):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def push(self, message, view_type=None, notification_type='',
             article='', image='', url='', latitude='', longitude=''):
        '''
        This method is the Chuck Norris of Push.co.
        It allows you the put a Push Notification in our queue
        we will do the rest by sending it to the Push.co app.
        This method has quite some options on how to display your notification.
        It should cover your needs.

        view_type values 0, 1, 2

        Value: 0
        Message View.
        Shows the notification with optional some additional content or image.

        Value: 1
        Web View. Combined with the send URL
        it'll display the contents in a UIWebView.
        In other words, the app will display the webpage specified in the URL.

        Value: 2
        Map View. Place a pin with the message on a map.
        '''
        if view_type == 0:
            self.push_message(message, article, image, notification_type)
        elif view_type == 1:
            self.push_web(message, url, notification_type)
        elif view_type == 2:
            self.push_map(message, latitude, longitude, notification_type)
        else:
            self.push_message(message, 0, notification_type)

    def push_message(self, message, article='', image='',
                     notification_type=''):
        '''
        Push a simple message
        required: message
        '''
        view_type = 0
        data = dict(message=message,
                    view_type=view_type,
                    notification_type=notification_type,
                    article=article,
                    image=image)
        return self._push_request(data)

    def push_web(self, message, url,
                 notification_type=''):
        '''
        Push a web message
        required: message, url
        '''
        view_type = 1
        data = dict(message=message,
                    view_type=view_type,
                    notification_type=notification_type,
                    url=url)
        return self._push_request(data)

    def push_map(self, message, latitude, longitude,
                 notification_type=''):
        '''
        Push a map message
        required: message, latitude, longitude
        '''
        view_type = 2
        data = dict(message=message,
                    view_type=view_type,
                    notification_type=notification_type,
                    latitude=latitude,
                    longitude=longitude)
        return self._push_request(data)

    def _push_request(self, data):
        data['api_key'] = self.api_key
        data['api_secret'] = self.api_secret
        data = requests.post(PUSH_URL, data)
        return data.json()
