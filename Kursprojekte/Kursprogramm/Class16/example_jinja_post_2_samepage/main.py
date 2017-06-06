#!/usr/bin/env python
import os
import jinja2
import webapp2


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
    user_input = ""
    user_input2 = ""

    def get(self):
        return self.render_template("hello.html", params={'user_input':self.user_input,
                                                          'user_input2': self.user_input2})

    def post(self):
        result = self.request.get("some_text")
        result2 = self.request.get("some_text2")

        self.user_input = result
        self.user_input2 = result2


        return self.render_template("hello.html",
                                    params={'user_input':self.user_input,
                                            'user_input2':self.user_input2})



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')


if __name__ == '__main__':
    main()
