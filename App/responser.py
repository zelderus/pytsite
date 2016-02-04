import zetypes
import sitetypes
import os
import sys, errno




def readFile(fileName):
	cnt = ""
	try:
		with open(fileName, 'r') as f1:
			cnt=f1.read()
	except IOError as e:
		if e.errno == errno.EPIPE:
			cnt += ""
	return cnt




#
#	Движок сайта
#
def createResponseHtml(serverWithoutFile, response, request):
	appPath = os.path.dirname(os.path.abspath(__file__))

	response.setTitle("ZeSite. Работа с Расберри")
	###
	# routing
	###
	controller = sitetypes.ZeController(request, response)
	path = request.getPath()


	if serverWithoutFile == True:
		# ignoring
		if path == "/favicon.ico": 
			response.error404() 
			return
		# content
		if path.startswith("/Content/jquery.js"): 
			response.responseAsScript()
			cnt = readFile(appPath + "/Content/jquery.js")
			response.write(cnt)
			return
		if path.startswith("/Content/site.js"): 
			response.responseAsScript()
			cnt = readFile(appPath + "/Content/site.js")
			response.write(cnt)
			return
		if path.startswith("/Content/site.css"): 
			response.responseAsStyle()
			cnt = readFile(appPath + "/Content/jquery.css")
			response.write(cnt)
			return




	# PAGES
	if path == "/": 
		response.write("<h1>Main page</h1>")
		return

	if path == "/test": 
		response.write("<h1>Test page</h1>")
		return




	# отдаем 404 если не обработали
	response.error404()
	return response