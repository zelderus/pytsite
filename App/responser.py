import Objects.zetypes as zetypes
import Objects.sitetypes as sitetypes
import os
import sys, errno
import zehelpers


from Controllers import *
#import Controllers as cts
#from Controllers import Controllers
#import Controllers.BaseController as bcont

#from os.path import dirname, basename, isfile
#import glob
#modules = glob.glob(dirname(os.path.abspath(__file__))+"/Controllers"+"/*.py")
#moduleNames = [ "Controllers."+basename(f)[:-3] for f in modules if isfile(f)]
#mdls = map(__import__, moduleNames)




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
	appPath = response.getAppPath() #os.path.dirname(os.path.abspath(__file__))

	response.setTitle("ZeSite")
	###
	# routing
	###
	controller = 0 #sitetypes.ZeController(request, response)
	controllerName = ""
	actionName = "show"
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




	# PAGES (from file 'routes')
	with open(appPath + "/Configs/routes", 'r') as routesFile:
			fcc = routesFile.readlines()
			for fline in fcc:
				if zehelpers.isNotNull(fline) == True and fline.startswith("#") == False:
					pp = fline.split(" ")
					if len(pp) >= 3 and path == pp[0]:
						controllerName = pp[1].replace("\n", "")
						actionName = pp[2].replace("\n", "").lower()


	# create controller
	if controllerName:
		try:
			klass = globals()[controllerName]
			controller = klass(request, response)
		except KeyError as e:
			print(e)
			response.error500("Ошибка построения контроллера: " + str(e))
			return
		

	# 404
	if controller == 0:
		response.error404()
		return



	# VIEW
	# check action name
	actionName = actionName.lower()
	if (actionName == "view"):
		esponse.error500("Ошибка в названии Action '" + actionName + "', нельзя использовать как имя действия.")
		return
	action = None
	try:
		action = getattr(controller, actionName)
	except AttributeError as e:
		print(e)
		response.error500("Ошибка построения действия котроллера: " + str(e))
		return
	# Action Do
	if action:
		controller.globalActionDo()
		action()




	return response # УСТАРЕЛО (по факту возвращаемое значение не используется более)