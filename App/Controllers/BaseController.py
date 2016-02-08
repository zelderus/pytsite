
import Objects.sitetypes as sitetypes


#
#	Стартовый контроллер
#	каждый контроллер должен быть прописан в __init.py__
#
class BaseController(sitetypes.ZeController):
	def __init__(self, request, response):
		sitetypes.ZeController.__init__(self, request, response)
		self.data = []


	#
	# Globals (for helpers)
	#
	def doMainMenu(self):
		request = self.getRequest()
		url = request.getPath()
		self.addToModel("menu_main_class", ("current" if url == "/" else ""))
		self.addToModel("menu_help_class", ("current" if url == "/help" else ""))
		self.addToModel("menu_test_class", ("current" if url == "/test" else ""))



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

