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

class Person(object):
    def__init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name


class MainHandler(BaseHandler):
    old_inputs = []
    numbers_list = []

    def get(self):
        return self.render_template("hello.html", params={'old_inputs':self.old_inputs})

    def post(self):

        result = self.request.get("some_text")
        result2 = self.request.get("some_number")

        if result:
            self.old_inputs.append(result)
        else:
            self.numbers_list.append(str(random.randint(1,100)))

        return self.render_template("hello.html", params={'old_inputs':self.old_inputs,
                                                          'numbers_list': self.numbers_list})
class subsiteHandler(BaseHandler):
    def get(self):
        self.render_template("Hello2.html")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/subsite', SubsiteHandler)
], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')


if __name__ == '__main__':
    main()
