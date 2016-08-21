from tornado.ioloop import IOLoop
from tornado.gen import coroutine
from tornado.gen import sleep



def A():
    def C(*args):
        print 'down'
    future = B()
    future.add_done_callback(C)
    IOLoop.current().start()

@coroutine
def B():
    yield sleep(5)

A()

'''
output: 
	coroutine sleep 5 second start
	coroutine sleep 5 second end
	down
'''
