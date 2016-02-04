from cgi import parse_qs, escape
import datetime


class ZeRequest:
	def __init__(self):
		self.data = []
		self.headers = {}
		self.params = {}
		self.path = "/"


	def setHeaders(self, headers):
		self.headers = headers
	def getHead(self, headKey):
		if headKey in self.headers:
			return self.headers[headKey]
		return ""

	def setParams(self, params):
		self.params = params
	def hasParam(self, paramKey):
		if paramKey in self.params:
			return True
		return False
	def getParam(self, paramKey):
		if self.hasParam(paramKey):
			return escape(self.params[paramKey]) # предохраняемся от инъекций
		return ""

	def setPath(self, pathStr):
		self.path = pathStr
	def getPath(self):
		return self.path





class ZeResponse:
	def __init__(self):
		self.request = [] #zetypes.ZeRequest
		self.selfContent = False
		# response header
		self.httpVer = "HTTP/1.1"
		self.status = "200 OK"
		self.server = "ZeServer pyth"
		self.contentType = "text/html; charset=utf-8"
		self.contentLength = 0
		self.acceptRanges = "bytes"
		self.connectionEnd = "keep-alive" #"close"
		# response body
		self.headTitle = "ZeSite"
		self.headStylesText = ""
		self.headScriptText = ""
		self.scriptLinks = []
		self.styleLinks = []
		self.body = ""


	def setRequest(self, request):
		self.request = request

	def getRequester(self):
		return self.request

	def getContent(self):
		return self.content

	def write(self, htmlStr):
		self.body += htmlStr 


	def error404(self):
		self.status = "404 Not Found"
		self.setTitle("Страница не найдена")
		self.write("<div style='margin: 60px 0; text-align: center;'>")
		self.write("<h1>404</h1>")
		self.write("<div>страница не найдена..</div>")
		self.write("</div>")


	def setContentAsScript(self):
		self.contentType = "application/x-javascript"
	def keepAlive(self):
		self.connectionEnd = "keep-alive"
	def connectionClose(self):
		self.connectionEnd = "close"

	def responseAsScript(self):
		self.selfContent = True
		self.setContentAsScript()
		self.keepAlive()
	def responseAsStyle(self):
		self.selfContent = True
		self.keepAlive()




	def setTitle(self, titleStr):
		self.headTitle = titleStr



	# добавление стиля (непосредственно текст стиля)
	def addStyleStr(self, styleStr):
		self.headStylesText += styleStr 
	# добавление скрипта (непосредственно текст скрипта)
	def addScriptStr(self, scriptStr):
		self.headScriptText += scriptStr 

	# добавление стиля ссылки (НЕ ИСПОЛЬЗУЕТСЯ)
	def addStyle(self, styleLink):
		self.styleLinks.push(scriptLink)
	# добавление скрипта ссылки (НЕ ИСПОЛЬЗУЕТСЯ)
	def addScript(self, scriptLink):
		self.scriptLinks.push(scriptLink)




	# построение контента ответа
	def buildGetHtmlBody(self):
		content = "<!DOCTYPE html>";
		content += "<html>"
		content += "<head>"
		content += "<title>"+ self.headTitle +"</title>"
		content += "<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>"
		content += "<meta http-equiv='X-UA-Compatible' content='IE=edge,chrome=1'>"

		content += "<link href='/Content/site.css' media='screen' rel='stylesheet'>"
		content += "<script src='/Content/jquery.js'></script>"
		content += "<script src='/Content/site.js'></script>"

		content += "<style type='text/css'>"+self.headStylesText+"</style>"
		content += "<script type='text/javascript'>$(function () {"
		content += self.headScriptText
		content += "});</script>"
		content += "</head>"
		content += "<body>"
		content += self.body
		content += "</body>"
		content += "</html>"
		return content




	#
	#	Полный ответ с заголовками и прочим
	#
	def buildHttpResponse(self):
		response = "";
		newLineStr = "\r\n"
		# response body
		html = ""
		if self.selfContent == False:
			html = self.buildGetHtmlBody()
		else:
			html = self.body
		# response header
		self.contentLength = len(html);
		dateNow = datetime.datetime.now()
		dateStr = str(dateNow) #"Mon, 18 Apr 2005 16:38:00 GMT" # TODO: !!!!!! to correct format
		lastDateStr = dateStr
		response += self.httpVer + " " + self.status + newLineStr
		response += "Date: " + dateStr + newLineStr
		response += "Server: " + self.server + newLineStr
		#response += "Last-Modified: " + lastDateStr + newLineStr
		#response += "Accept-Ranges: " + self.acceptRanges + newLineStr
		#response += "Content-Length: " + str(self.contentLength) + newLineStr
		response += "Content-Type: " + self.contentType + newLineStr
		response += "Cache-Control: no-cache" + newLineStr
		response += "Connection: " + self.connectionEnd + newLineStr + newLineStr
		response += html
		response += newLineStr + newLineStr + newLineStr
		
		return response

