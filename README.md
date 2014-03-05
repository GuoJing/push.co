push.co / pushcoapi
=======

Python lib for push.co, called `pushcoapi`, this is very simple and support all API of push.co, just see demo.py!

Easy interface for you:

1. push_message
2. push_web
3. push_map

**APP**

Try push.co app:


![pushcoapi](http://guojing.me/images/2014/push.co.png)

**Simple for authorize**

    def auth():
        from pushcoapi.authorize import Authorize

        auth = Authorize(api_key, api_secret, redirect_url)

        url = auth.get_auth_url()
        print '1. Go to link below'
        print '2. Click Allow'
        print '3. Copy the authorization code.'
        print url
        code = raw_input("Enter the authorization code here: ").strip()

        data = auth.get_access_token(code)

        print data

        access_token = data.get('access_token')

        data = auth.check_access_token(access_token)

        print data

        #data = auth.delete_access_token(access_token)

        #print data
        return access_token

**Simple for subscription**

    def subscription(access_token):
        from pushcoapi.subscription import Subscription
        s = Subscription(access_token)
        print s.gets()

**Simple for push!**

    def push():
        from pushcoapi.push import Push
        p = Push(api_key, api_secret)
        ret = p.push_message('Hello, this is a message from demo')
        print ret

        ret = p.push_web('Hello, this is a web', 'http://guojing.me')
        print ret

        ret = p.push_map('Hello, this is a map', '39.9026266648', '116.4012871818')
        print ret

**Install**

    pip install pushcoapi