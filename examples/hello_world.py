from wsgiref import simple_server
from kettle.application import Application


def hello(request, response):
    print(request.query_params)
    return response.send('Hello World!!')


def hello_post(request, response):
    print(request.data)
    return response.send('Hello POST!!')


def ham(request, response):
    print(request.actions)
    return response.send('ham egg spam')

application = Application()
application.router.register('GET', '/', hello)
application.router.register('POST', '/', hello_post)
application.router.register('PUT', '/', hello_post)
application.router.register('GET', '/hams/', ham)
application.router.register('GET', '/hams/:ham_id/eggs/:egg_id/', ham)

if __name__ == '__main__':
    httpd = simple_server.make_server('', 8000, application)
    httpd.serve_forever()
