import tornado.ioloop
import tornado.web

from .route import ROUTES


def make_app():
    return tornado.web.Application(ROUTES)


app = make_app()
app.listen(8080)
tornado.ioloop.IOLoop.current().start()