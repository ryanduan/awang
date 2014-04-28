import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print self.request.uri
        print self._transforms
        self.write("Hello, world")



if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/awang/?", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
