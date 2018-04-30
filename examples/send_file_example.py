from wsgiref import simple_server
import os
from kettle.application import Application


def download_file(request, response):
    filename = request.query_params.get('filename')
    if filename:
        target = os.path.join('uploads', filename[0])
        return response.file(target)
    return response.json('file not found', status=404)


def upload_file(request, response):
    file_data = request.form['newfile'].file
    filename = request.form['newfile'].filename
    target = os.path.join('uploads', filename)
    f = open(target, 'wb')
    while True:
        buf = file_data.read()
        if not buf:
            break
        f.write(buf)
    f.close()
    return response.text('Success: {}'.format(filename))


application = Application()
application.router.register('GET', '/', download_file)
application.router.register('POST', '/', upload_file)

if __name__ == '__main__':
    httpd = simple_server.make_server('', 8000, application)
    httpd.serve_forever()
