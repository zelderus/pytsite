
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
		# title
		response.setTitle("ZeSite. Test")
		# get param
		p1 = request.getParam("p1")
		# show
		self.view("show", dict(p1=p1, modelVal1="just simple"))


