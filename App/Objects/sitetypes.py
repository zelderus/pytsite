

import Objects.zetypes as zetypes
import zehelpers
import re



#
#	Контроллер
#
class ZeController:
	def __init__(self, request, response):
		self.request = request
		self.response = response
		self._model = None

	def getRequest(self):
		return self.request

	def getResponse(self):
		return self.response



	def _modelRepl(self, matchobj):
		return self._zrGetModelValue(self._model, matchobj.group(1))
	# значение из модели
	def _zrGetModelValue(self, model, valName):
		if model == None or model.__class__.__name__ != "dict":
			return ""
		if valName in model:
			return model[valName]
		return ""
	# парсилка строки Вьюшки
	def _zrParseLine(self, lineStr, model):
		lineStr = re.sub("@{(\w+)}", self._modelRepl, lineStr)
		return lineStr


	# достаем файл Вьюшку, парсим и записываем в контент
	def view(self, viewName=None, model=None, controllerName=None):
		self._model = model
		if controllerName == None:
			controllerName = self.__class__.__name__
		controllerName = controllerName.replace(' ', '').lower()
		if controllerName.endswith("controller"):
			controllerName = controllerName[:-10]
		if viewName == None:
			viewName = "show"
		viewName = viewName.replace(' ', '').lower()
		response = self.getResponse()
		try:
			with open(response.getAppPath() + "/Views/" + controllerName + "/" + viewName + ".zr.html", 'r') as viewFile:
				fcc = viewFile.readlines()
				for fline in fcc:
					if zehelpers.isNotNull(fline) == True and fline.startswith("#") == False:
						response.write(self._zrParseLine(fline, model))
		except BaseException  as e:
			print("Error in Action")
			self.response.error500("Ошибка выполнения во Вьюшке: " + str(e))
			return



	# пример действия
	def show(self):
		#return self.view("Test")
		self.getResponse().write("empty")
