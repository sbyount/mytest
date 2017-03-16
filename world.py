
def func1():
    print
    print "Hello World"
    print

class MyClass(object):
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def hello(self):
        print "Hello World: {} {} {}".format(self.var1, self.var2, self.var3)

    def not_hello(self):
        print "Goodbye: {} {} {}".format(self.var1, self.var2, self.var3)

class MyChildClass(MyClass):
    '''
    Test class augmenting __init__
    Could use super() also
    '''
    def __init__(self, var1, var2, var3):
        print "Do something more in __init__()"
        MyClass.__init__(self, var1, var2, var3)

    def hello(self):
        print "Something else: %s %s %s" % (self.var1, self.var2, self.var3)

if __name__ == '__main__':
    print "Main program - Hello World"
    print

    # Test Code
    print "MyClass output"
    my_obj = MyClass('SAT', 'DFW', 'HOU')
    print my_obj.var1, my_obj.var2, my_obj.var3
    my_obj.hello()
    my_obj.not_hello()
    print

    # Test Code
    print "MyChildClass output"
    my_obj = MyChildClass('X', 'Y', 'Z')
    my_obj.hello()
    my_obj.not_hello()
    print
