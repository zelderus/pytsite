
import Objects.sitetypes as sitetypes


#
#	Стартовый контроллер
#	каждый контроллер должен быть прописан в __init.py__
#
class BaseController(sitetypes.ZeController):
	def __init__(self, request, response):
		sitetypes.ZeController.__init__(self, request, response)
		self.data = []


	def getMenuModel(self, model=None):
		if model == None:
			model = dict()
		request = self.getRequest()
		url = request.getPath()
		model["menu_main_class"] = ("current" if url == "/" else "")
		model["menu_help_class"] = ("current" if url == "/help" else "")
		model["menu_test_class"] = ("current" if url == "/test" else "")
		return model



	def show(self):
		response = self.getResponse()
		request = self.getRequest()
		response.setTitle("ZeSite")
		model = self.getMenuModel()
		self.view("show", model)
		


	def help(self):
		response = self.getResponse()
		request = self.getRequest()
		response.setTitle("ZeSite. Help")
		model = self.getMenuModel()
		self.view("help", model)


	def about(self):
		response = self.getResponse()
		request = self.getRequest()
		response.setTitle("ZeSite. About")
		model = self.getMenuModel()
		self.view("about", model)

