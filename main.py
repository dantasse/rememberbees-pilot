#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import logging, os, random
from google.appengine.ext import db

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Answers(db.Model):
    q1 = db.StringProperty()
    q2 = db.StringProperty()
    q3 = db.StringProperty()
    q4 = db.StringProperty()
    q5 = db.StringProperty()
    q6 = db.StringProperty()
    q7 = db.StringProperty()
    q8 = db.StringProperty()
    q9 = db.StringProperty()
    q10 = db.StringProperty()
    name = db.StringProperty()
    user_number = db.IntegerProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))


class AnswersHandler(webapp2.RequestHandler):
    def post(self):
        # Random ID is fine; only testing a few subjects
        number = random.randint(1, 1000000)

        answers = Answers()
        answers.q1 = self.request.get('q1')
        answers.q2 = self.request.get('q2')
        answers.q3 = self.request.get('q3')
        answers.q4 = self.request.get('q4')
        answers.q5 = self.request.get('q5')
        answers.q6 = self.request.get('q6')
        answers.q7 = self.request.get('q7')
        answers.q8 = self.request.get('q8')
        answers.q9 = self.request.get('q9')
        answers.q10 = self.request.get('q10')
        answers.name = self.request.get('name')
        answers.user_number = number
        answers.put()

        template_values = {
            'number': number
        }
        template = jinja_environment.get_template('thankyou.html')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/answers', AnswersHandler),
], debug=True)
