
import Objects.sitetypes as sitetypes
from Controllers import BaseController

#
#	Test
#	каждый контроллер должен быть прописан в __init.py__
#
class TestController(BaseController):
	def __init__(self, request, response):
		BaseController.__init__(self, request, response)
		self.data = []



	def show(self):
		response = self.getResponse()
		request = self.getRequest()
		# title
		response.setTitle("ZeSite. Test")
		# get param
		p1 = request.getParam("p1")
		# model (best use global model 'self.addToModel()')
		model = dict()
		model["p1"] = p1
		self.addToModel("modelVal1", "just simple global")
		model["modelVal1"] = "just simple page"

		# show
		self.view("show", model)


