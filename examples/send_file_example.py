from wsgiref import simple_server import os
from kettle.application import Application


def hello(request, response):
    print(request.query_params)
    return response.text('Hello World!!')


def hello_post(request, response):
    file_data = request.form['newfile'].file
    filename = request.form['newfile'].filename
    # write the content of the uploaded file to a local file
    target = os.path.join('uploads', filename)
    f = open(target, 'wb')
    while True:
        buf = file_data.read()
        if not buf:
            break
        f.write(buf)
    f.close()
    return response.text('Hello POST!!')


def ham(request, response):
    print(request.actions)
    return response.text('ham egg spam')

application = Application()
application.router.register('GET', '/', hello)
application.router.register('POST', '/', hello_post)
application.router.register('PUT', '/', hello_post)
application.router.register('GET', '/hams/', ham)
application.router.register('GET', '/hams/:ham_id/eggs/:egg_id/', ham)

if __name__ == '__main__':
    httpd = simple_server.make_server('', 8000, application)
    httpd.serve_forever()
