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
import cgi
form="""
<form method="post">
	What is your birthday?
	<br>
	<label> Month
	<input type="text" name="month" value="%(month)s">
	</label>
	<label> Day
	<input type="text" name="day" value="%(day)s">
	</label>
	<label> Year
	<input type="text" name="year" value="%(year)s">
	<label>
	<br>
	<div style="color: red">%(error)s</div>
<input type="submit">
</form>
"""
def escape_html(s):
    # for(i, o) in (("&", "&amp;"),(">", "&gt;"),("<", "&lt;"),('"', "&quote;")):
		# s = s.replace(i, o)
	# return s
	return cgi.escape(s, quote = True)
	
class MainPage(webapp2.RequestHandler):
	months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
	mon = dict((m[:3].lower(),m) for m in months)
	def valid_month(month):
		if month:
			short = month[:3].lower()
			return mon.get(short)
		# cap = month.capitalize()
		# if cap in months:
			# return cap
	
	def valid_day(day):
		if day and day.isdigit():
			d = int(day)
			if d > 0 or d <= 31:
				return d
			
	def valid_year(year):
		if year and year.isdigit():
			y = int(year)
			if y >= 1900 and y <= 2020:
				return y
	
	def write_form(self, err="", mon="", dy="", yr=""):
		self.response.out.write(form % {"error": err,
										"month": escape_html(mon),
										"day": escape_html(dy),
										"year": escape_html(yr)})
	
    def get(self):
        #self.response.write('Hello world!!!!')
		#self.response.headers['Content-Type'] = 'text/plain'
		#self.response.out.write(form)
		self.write_form()
		
	def post(self):
		# user_month = valid_month(self.request.get('month'))
		# user_day = valid_day(self.request.get('day'))
		# user_year = valid_year(self.request.get('year'))
		user_month = self.request.get('month')
		user_day = self.request.get('day')
		user_year = self.request.get('year')
		month = valid_month(user_month)
		day = valid_day(user_day)
		year = valid_year(user_year)
		
		#if not (user_day and user_month and user_year):
		if not (day and month and year):
			#self.response.out.write(form)
			self.write_form("it is not valid!", user_month, user_day, user_year)
		else:
			self.redirect("/thanks")

			
class thanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Thanks! that's a valid input")
	
app = webapp2.WSGIApplication([('/', MainPage), ('/thanks', thanksHandler)], debug=True)
		
#class TestHandler(webapp2.RequestHandler):
#	def post(self):
#		s = self.request.get("p")
#		self.response.out.write(s)
		#self.response.headers['Content-Type'] = 'text/plain'
		#self.response.out.write(self.request)

		#('/testform',TestHandler)
