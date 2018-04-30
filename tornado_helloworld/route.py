from .view import MainHandler
#  from tornado.routing import Rule, PathMatches

ROUTES = [
    (r"/(.*)", MainHandler)  # Rule(PathMatches(r"/(.*)"), MainHandler)
]