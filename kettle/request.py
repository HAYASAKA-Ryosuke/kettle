import urllib
import cgi


class Request:
    def __init__(self, environ, actions):
        self.META = environ
        self.actions = actions
        if self.META.get('CONTENT_TYPE', '').startswith('multipart/'):
            self._form = cgi.FieldStorage(environ=self.META, fp=self.META.get('wsgi.input'), encoding='utf8', keep_blank_values=True)
        else:
            self._form = None

    @property
    def query_params(self):
        if self.META.get('REQUEST_METHOD') == 'GET':
            return urllib.parse.parse_qs(self.META['QUERY_STRING'])

    @property
    def form(self):
        form = self._form
        return form

    @property
    def data(self):
        if self.META.get('REQUEST_METHOD') in ['POST', 'PUT', 'DELETE', 'PATCH']:
            content_length = int(self.META.get('CONTENT_LENGTH'))
            return self.META['wsgi.input'].read(content_length).decode('utf8')
