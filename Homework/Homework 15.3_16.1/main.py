#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import jinja2
import webapp2
import random

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")


class LotteryHandler(BaseHandler):
    def get(self):

        lotto = sorted(random.sample(range(1, 45), 6))
        params = {"lotto": lotto}

        return self.render_template("Lotteryagain.html", params=params)


class CalculatorHandler(BaseHandler):
    def get(self):
        return self.render_template("Calculator.html")

    def post(self):

        num1 = float(self.request.get("num1"))
        num2 = float(self.request.get("num2"))
        operation = self.request.get("chooser")

        solve = 0

        if operation == "+":
            solve = num1 + num2
        elif operation == "-":
            solve = num1 - num2
        elif operation == "*":
            solve = num1 * num2
        elif operation == "/":
            solve = num1 / num2

        return self.write("This makes %s" % solve)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/Lotteryagain', LotteryHandler),
    webapp2.Route('/Calculator', CalculatorHandler),
], debug=True)

