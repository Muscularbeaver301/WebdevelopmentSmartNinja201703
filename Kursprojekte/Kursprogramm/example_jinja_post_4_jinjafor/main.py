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
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class MainHandler(BaseHandler):
    persons = []

    def get(self):
        return self.render_template("hello.html", params={'persons_list':self.persons})

    def post(self):

        first_name = self.request.get("first_name")
        last_name = self.request.get("last_name")
        new_person = Person(first_name,last_name)
        self.persons.append(new_person)

        return self.render_template("hello.html", params={'persons_list':self.persons})



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler)
], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')


if __name__ == '__main__':
    main()
