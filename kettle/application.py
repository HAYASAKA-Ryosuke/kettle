from .router import Router
from .request import Request
from .response import Response


class Application:
    def __init__(self):
        self.router = Router()

    def __call__(self, environ, start_response):
        view, actions = self.router.search(environ.get('REQUEST_METHOD'), environ.get('PATH_INFO', '/'))

        if view is None:
            response = Response().text('404 not found', 404)
        else:
            response = view(Request(environ, actions), Response())

        start_response(response.status, response.headers)
        return [response.body]
