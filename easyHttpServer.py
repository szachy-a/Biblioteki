import flask
import functools

_app = flask.Flask(__name__)

def addPath(path):
    def add(f):
        def newFun():
            return f(**{k:f.__annotations__.get(k, str)(v) for k, v in dict(flask.request.args).items()})
        _app.route(path)(newFun)
        return f
    return add

def run(port : int):
    _app.run(port=port)

if __name__ == '__main__':
    import html
    import moje
    v = None
    @addPath('/')
    def f():
        return '/'
    @addPath('/somesite')
    def g(h='qwerty'):
        return '/somesite?' + h
    run(80)
