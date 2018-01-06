import urllib


class Request:
    def __init__(self, environ, actions):
        self.META = environ
        self.actions = actions

    @property
    def query_params(self):
        if self.META.get('REQUEST_METHOD') == 'GET':
            return urllib.parse.parse_qs(self.META['QUERY_STRING'])

    @property
    def data(self):
        if self.META.get('REQUEST_METHOD') in ['POST', 'PUT', 'DELETE', 'PATCH']:
            content_length = int(self.META.get('CONTENT_LENGTH'))
            return self.META['wsgi.input'].read(content_length).decode('utf8')
