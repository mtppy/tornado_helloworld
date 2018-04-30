import tornado.web


class MainHandler(tornado.web.RequestHandler):

    async def get(self, name=''):
        self.write("Hello, {}".format(name))