
import Objects.sitetypes as sitetypes



#
#	Test
#	каждый контроллер должен быть прописан в __init.py__
#
class TestController(sitetypes.ZeController):
	def __init__(self, request, response):
		sitetypes.ZeController.__init__(self, request, response)
		self.data = []



	def show(self):
		response = self.getResponse()
		request = self.getRequest()


		p1 = request.getParam("p1")

		response.setTitle("ZeSite. Test")
		response.write("<h1>Test page</h1>")
		response.write("<div>P1="+p1+"</div>")