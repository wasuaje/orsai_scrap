import urllib
import urllib2



def fill_form(valor):
	url = 'http://orsai.bitacoras.com/wp-comments-post.php'
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
        referer = "http://orsai.bitacoras.com/"

	submitVars={}
	submitVars['author'] = "Wuelfhis Asuaje"
	submitVars['email'] = "wasuaje@hotmail.com"
	submitVars['comment'] = "<b>PRI</b>  Excelente. Saludos desde Venezuela !"
	submitVars['comment_post_ID'] = valor
	submitVars['comment_parent'] = "0"

	submitUrl = url

	submitVarsUrlencoded = urllib.urlencode(submitVars)
	req = urllib2.Request(submitUrl, submitVarsUrlencoded)
	req.add_header('Referer', referer)
	req.add_header('User-Agent', user_agent)

	response = urllib2.urlopen(req)
	thePage = response.read()

#['        <div class="texto_seccion"', '<a href="http://orsai.bitacoras.com/category/bar" title="Ver todas las entradas en Bar" rel="category tag"',
# 'Bar</a', ', <a href="http://orsai.bitacoras.com/category/revista" title="Ver todas las entradas en Revista" rel="category tag"', 'Revista</a', '</div',
# '        <div class="texto_gran_titulo"', '<a href="http://orsai.bitacoras.com/2011/09/voragine-de-noticias.php"', 'Vor\xc3\xa1gine de noticias</a',
# '</div', '']


def read_main():
	req = urllib2.urlopen('http://orsai.bitacoras.com')
	data =req.read()
	datar=data.split('\r\n')
	nuevo=""
	pagina=""

	for i in range(len(datar)):
		if "texto_seccion" in datar[i]:
			seccion=datar[i].split('>')
			break

	for h in range(0,len(seccion)):		
		if "texto_gran_titulo" in seccion[h]:
	    #    	print "valor de h "+str(h)
			nuevo  = seccion[h+2].replace('</a','')			# nombre del nuevo post
#.split('>')[6]
			pagina = seccion[h+1].replace('<a href=','').replace('"','') 	# direccion del nuevo post
#.split('>')[5]

	#print "nuevo",nuevo
	#print "pagina",pagina
	return nuevo,pagina


fp = open("orsay.dat")
viejo=fp.read()
fp.close()

nuevo,urlnew=read_main()
while nuevo=='' or urlnew=='':
	nuevo,urlnew=read_main()


req = urllib2.urlopen(urlnew)								# direccion del nuevo post
data =req.read()
datas=data.split('\r\n')

for i in range(len(datas)):
	if "comment_post_ID" in datas[i]:
		valor=datas[i].split('<input')						# saco la linea donde esta el nro de post
for h in range(len(valor)-1):
	if "comment_post_ID" in valor[h]:
		valor = valor[h].split(' ')[3]
		valor = valor.replace("value='",'').replace("'",'')			# saco el nro de post en limpio

if nuevo<>viejo:
	fp = open("orsay.dat",'w')
	fp.write(nuevo)
	fp.close()
	fill_form(valor)
	print nuevo
	print urlnew
	print valor
	
