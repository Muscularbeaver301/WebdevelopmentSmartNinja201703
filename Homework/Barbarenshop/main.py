import os
import time
import datetime
import jinja2
import webapp2
from google.appengine.api import users

import currency_scraper

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

class BaseHandler(webapp2.RequestHandler):
    # comes with
    # .request

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    # with params as dict
    def _render_str(self, template, params):
        jinja = jinja_env.get_template(template)
        return jinja.render(params)

    def render_template(self, template, params={}):
        a = self._render_str(template, params)
        self.write(a)

    # with params as unpacked dict
    def render_str(self, template, **params):
        jinja = jinja_env.get_template(template)
        return jinja.render(params)

    def render(self, template, **params):
        a = self.render_str(template, **params)
        self.write(a)

################################################################################

def f(x,y):
    r = float(x) + float(y)
    return r

class FriseurHandler(BaseHandler):
    def get_params(self):
        time_now = time.strftime("%d.%m 20%y at %H:%M and %S seconds")
        #date = time.date()
        prices = currency_scraper.get_prices()
        ps = {'time_now': time_now, 'myboolean': True, 'prices': prices}
        google_user = users.get_current_user()
        if google_user:
            nickname = google_user.nickname()
            ps.update({'nickname': nickname})
        return ps

    def get(self):
        ps = self.get_params()
        self.render_template("friseur.html", params=ps)

class MartinHandler(BaseHandler):
    def get(self):
        r = 0
        ps = {"result": r}
        self.render_template("Martin.html", params=ps)

    def post(self):
        x = self.request.get('num1')
        y = self.request.get('num2')
        r = f(x,y)
        ps = {"result": r}
        self.render_template("Martin.html", params=ps)

class NikolajHandler(BaseHandler):
    def get(self):
        self.render_template("Nikolaj.html")

class MikeHandler(BaseHandler):
    def get(self):
        self.render_template("Mike.html")

class CoffeeHandler(BaseHandler):
    def get(self):
        self.render_template("coffee.html")

app = webapp2.WSGIApplication(
    [webapp2.Route('/', FriseurHandler)

    ,webapp2.Route('/Mike', MikeHandler)
    ,webapp2.Route('/Nikolaj', NikolajHandler)
    ,webapp2.Route('/Martin', MartinHandler)
    ,webapp2.Route('/coffee', CoffeeHandler)
    ]
, debug=True)
