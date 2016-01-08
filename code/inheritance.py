class First(object):
    def __init__(self):
        print "first"

class Second(object):
    def __init__(self):
        print "second"

class Third(object):
    def __init__(self):
        print "third"

class Fourth(First ,Second, Third):
    def __init__(self):
        super(Fourth, self).__init__()
        print "that's it"

a = Fourth()