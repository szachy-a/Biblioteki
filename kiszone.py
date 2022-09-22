def dumps(co):
    pass

def loads(co):
    pass

def dump(co, f):
    f.write(dumps(co))

def load(f):
    return loads(f.read())
