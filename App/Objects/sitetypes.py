

import Objects.zetypes as zetypes



#
#	Контроллер
#
class ZeController:
	def __init__(self, request, response):
		self.request = request
		self.response = response


	def getRequest(self):
		return self.request

	def getResponse(self):
		return self.response



	def show(self):
		self.getResponse().write("empty")