from wsgiref import simple_server
from kettle.application import Application
from kettle.response import Response


def hello(request):
    print(request.query_params)
    response = Response('Hello World!!')
    return response


def hello_post(request):
    print(request.data)
    response = Response('Hello POST!!')
    return response


def ham(request):
    response = Response('ham egg spam')
    print(request.actions)
    return response

application = Application()
application.router.register('GET', '/', hello)
application.router.register('POST', '/', hello_post)
application.router.register('PUT', '/', hello_post)
application.router.register('GET', '/hams/', ham)
application.router.register('GET', '/hams/:ham_id/eggs/:egg_id/', ham)

if __name__ == '__main__':
    httpd = simple_server.make_server('', 8000, application)
    httpd.serve_forever()
