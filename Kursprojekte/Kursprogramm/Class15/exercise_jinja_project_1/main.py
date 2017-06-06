#!/usr/bin/env python
import os
import jinja2
import webapp2

import random

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        global _Visitor
        return self.render_template("hello.html")

class TestHandler(BaseHandler):
    def get(self):
        return self.render_template("Testfile.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/subtestfile', TestHandler)
], debug=True)





#  Exercise 1: write a Handler, and an HTML page which links to a new page random.html


#  Exercise 2: each time this page is opened, pass a random number which should be displayed on the page


#  Exercise 3: create a folder in template, call it 'projects'.


#  Now integrate a page within the projects folder into your website

# Visitorcounter

