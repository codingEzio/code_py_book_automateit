import httplib2
import tornado.web
import tornado.ioloop

# This example won't work
#   Try some from the official doc will be better!
#   Right here: https://www.tornadoweb.org/en/stable/

class AsyncHandler(tornado.web.RedirectHandler):
	
	@tornado.web.asynchronous
	def get(self):
		http = httplib2.Http()
		self.resp, self.cont = http.request('http://ip.jsontest.com/', 'GET')
		self._async_callback(self.resp, self.cont)
	
	def _async_callback(self, resp, cont):
		print(f"Content: {cont}")
		print(f"Response:\nStatCode: {resp['status']} Location: {resp['content-location']}")
		
		self.finish()
		
		tornado.ioloop.IOLoop.instance().stop()
		
application = tornado.web.Application(
	[(r'/', AsyncHandler)],
	debug=True,
)

if __name__ == '__main__':
	application.listen(9999)
	tornado.ioloop.IOLoop.instance().start()