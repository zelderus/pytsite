
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
		response.setTitle("ZeSite")
		self.view("show")
		


	def help(self):
		response = self.getResponse()
		request = self.getRequest()
		response.setTitle("ZeSite. Help")
		self.view("help")


	def about(self):
		response = self.getResponse()
		request = self.getRequest()
		response.setTitle("ZeSite. About")
		self.view("about")

