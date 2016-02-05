
import sys
import os
import requester
import Objects.zetypes as zetypes
import responser
import sys, errno


# размер запроса
requestSize = 2048
# приложение сервер не умеет обрабатывать файлы контента (логика на сайте этом)
# если сервер умеет работать со статикой (аля nginx), то ставим False
# если сервер перенаправляет все запросы сюда, то True
# --- хотя если сервер перенаправляет запросы сам, то сюда дело не дойдет
serverWithoutFile = True




#
#	Из дескприптора файла читаем запрос и пишем в него ответ
#
def main():
	global requestSize
	global serverWithoutFile
	# дескриптор файла (что пришел по сокету с сервера с запросом)
	fd = int(sys.argv[1])
	print("--------")

	# запрос
	requestData = str(os.read(fd, requestSize)) #os.read(fd, 2048).decode('utf-8') #str(os.read(fd, 2048))

	# парсинг запроса
	request = requester.getHeaders(requestData)
	requester.parseParams(request)

	# ответl
	response = zetypes.ZeResponse();
	response.setAppPath(os.path.dirname(os.path.abspath(__file__)))	# root path (from main)
	response.setRequest(request)

	# content
	respDeprecatedVar = responser.createResponseHtml(serverWithoutFile, response, request)
	content = response.buildHttpResponse()


	#with open(fd, 'w') as outf:
	#	outf.write(content)
	try:
		with open(fd, 'w') as outf:
			outf.write(content)
	except IOError as e:
		if e.errno == errno.EPIPE:
			print("pipe err")



	print("ok")




#
#	Точка входа в приложение
#
main()