
import Objects.sitetypes as sitetypes


#
#	Стартовый контроллер
#	каждый контроллер должен быть прописан в __init.py__
#
class BaseController(sitetypes.ZeController):
	def __init__(self, request, response):
		sitetypes.ZeController.__init__(self, request, response)
		self.data = []




	def show(self):
		response = self.getResponse()
		request = self.getRequest()


		p1 = request.getParam("p1")

		response.setTitle("ZeSite")
		response.write("<h1>Main page</h1>")
		response.write("<div>P1="+p1+"</div>")


