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
import random

def getRandomFortune():
    fortunes = [
        "your luck will change in the near future"
        , "I see much code in   your future"
        ,"consider your future"
    ]
    selected_fortune = random.choice(fortunes)
    return selected_fortune
class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1> Fortune Cookie </h1>" 
        luckynumber = random.randint(1,100)
        numbersentence ='Your lucky number is ' + str(luckynumber) 
        numberparagraph = "<p>" + numbersentence + "</p>"
        
        cookie_again_button = "<a href = '.'> <button>Another cookie plz </button> </a>"

        fortune = getRandomFortune()
        fortune_sentence = "Your fortune: " + fortune
        fortune_paragraph = "<p>" + fortune + "</p>"

        content = header + fortune_paragraph + numberparagraph  + cookie_again_button
        self.response.write(content)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
   
    ], debug=True)
