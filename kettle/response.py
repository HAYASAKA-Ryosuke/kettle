class Response:

    STATUS = {200: '200 OK', 404: '404 Not Found', 400: '400 Bad Request'}

    def _send(self, body, status, headers):
        self.status = self.STATUS.get(status, 200)
        self.headers = headers
        self.body = body.encode('utf-8') if isinstance(body, str) else body
        return self

    def text(self, body='', status=200, headers=[('Content-type', 'text/html; charset=UTF-8')]):
        return self._send(body, status, headers)

    def json(self, body='', status=200):
        headers = [('Content-type', 'application/json; charset=UTF-8')]
        return self._send(body, status, headers)

    def file(self, file_path, status=200, headers=[('Accept-Ranges', 'bytes')]):
        return self._send(open(file_path, 'rb').read(), status, headers)
