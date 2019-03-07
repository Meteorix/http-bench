import rapidjson as json
import os


def app(env, start_response):
    path = env['PATH_INFO']
    if path == '/json':
        start_response('200 OK', [('Content-Type', 'application/json')])
        return [json.dumps({'message': 'Hello, world!'}).encode('utf-8')]

    start_response('404 Not Found', [('Content-Type', 'text/plain')])
    return [b'Not Found']

