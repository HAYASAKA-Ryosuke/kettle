from wsgiref import simple_server
from kettle.application import Application


def hello(request, response):
    print(request.query_params)
    return response.text('Hello World!!')


def hello_post(request, response):
    print(request.data)
    return response.text('Hello POST!!')


def ham(request, response):
    print(request.actions)
    return response.text('ham egg spam')

def redirect(request, response):
    return response.redirect('/hams/', 301)

application = Application()
application.router.register('GET', '/', hello)
application.router.register('POST', '/', hello_post)
application.router.register('PUT', '/', hello_post)
application.router.register('GET', '/hams/', ham)
application.router.register('GET', '/hams/:ham_id/eggs/:egg_id/', ham)
application.router.register('GET', '/redirect/', redirect)

if __name__ == '__main__':
    httpd = simple_server.make_server('', 8000, application)
    httpd.serve_forever()
