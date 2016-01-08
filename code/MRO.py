#http://stackoverflow.com/questions/1848474/method-resolution-order-mro-in-new-style-python-classes
class Base1(object):
    def amethod(self): print "Base1"

class Base2(Base1):
    pass

class Base3(Base1):
    def amethod(self): print "Base3"

class Derived(Base2,Base3):
    pass

instance = Derived()
instance.amethod()


class Base1:
    def amethod(self): print "Base1"

class Base2(Base1):
    pass

class Base3(Base1):
    def amethod(self): print "Base3"

class Derived(Base2,Base3):
    pass

instance = Derived()
instance.amethod()