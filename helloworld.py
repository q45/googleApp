import webapp2
import cgi

from google.appengine.api import users


class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("""
			<html>
				<body>
				<form action="/book" method="post">
					<div><textarea name="content" rows="3" cols="60"></textarea>
					<div><input type="submit" value="Sign Guestbook"></div>
				</form>
				</body>
			</html>""")
	

class Guestbook(webapp2.RequestHandler):
	def post(self):
		self.response.out.write('<html><body>You Wrote:<pre>')
		self.response.out.write(cgi.escape(self.request.get('content')))
		self.response.out.write('</pre></body></html>')


app = webapp2.WSGIApplication([('/', MainPage),
							  ('/book', Guestbook)],
							   debug=True)