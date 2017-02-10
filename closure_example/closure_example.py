def foo():
    m=3
    n=5
    def bar():
        a=4
        return m+n+a
    return bar

bar = foo()
print bar.__closure__
