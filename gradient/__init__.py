import requests
from requests.auth import HTTPBasicAuth

def factory(base_url, id, token):
    class Client:
        def __init__(self):
            self.base_url = "%s/api/subscriptions/%s" % (base_url, id)

        def format_url(self, resource = None, id = None):
            url = self.base_url
            if resource:
                url = "%s/%s" % ( url, resource )
                if id:
                    url = "%s/%s" % ( url, id )
            return url

        def auth(self):
            return HTTPBasicAuth( 'gradient', token )

        def get(self, resource = None, id = None):
            url = self.format_url( resource, id )
            print( url )
            return requests.get( url, auth=self.auth() )

        def post(self, body, resource = None, id = None):
            url = self.format_url( resource, id )
            return requests.post( url, auth=self.auth(), json=body )

    client = Client()
    return client
