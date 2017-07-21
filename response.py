class Response:

    STATUS = {200: '200 OK', 404: '404 Not Found', 400: '400 Bad Request'}

    def __init__(self, body='', status=200, headers=[('Content-type', 'text/html; charset=UTF-8')]):
        self.status = self.STATUS.get(status, 200)
        self.headers = headers
        self.body = body

    def params(self):
        if isinstance(self.body, str):
            self.body = self.body.encode('utf-8')
        return self.status, self.headers, self.body
