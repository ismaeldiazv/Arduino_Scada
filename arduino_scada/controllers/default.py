# -*- coding: utf-8 -*-

# Importamos las librerias
import serial
import time

# Funcion index
def index():
    	
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))
	
# Creamos un objeto de tipo serial que es el puerto al que esta conectado el arduino, cerramos el puerto y lo abrimos, para asegurarnos que esta libre
puerto_Serie=serial.Serial('/dev/ttyACM0', 115200)   # En windows COM34
puerto_Serie.close()
puerto_Serie.open()

# Funcion que ejecuta el post
def recibe_datos():
	
	# Declaramos las variables que vamos a utilizar
	cadena=''
	datos=[]
	# Obtenemos en valor lo que nos devuelve el post mediante request.vars y buscamos la clave Valor
	valor=str(request.vars.Valor)
	
	# Si lo que nos ha devuelto valor ha sido 1, cadena es 'a'
	if (valor=='1'):
		#db.valores.insert(valor=True)
		cadena='a'
		
	# Si lo que nos ha devuelto valor ha sido 0, cadena es 'b'
	if (valor=='0'):
		#db.valores.insert(valor=False)
		cadena='b'
	
	# Mandamos por puerto serie lo que vale la variable cadena 
	puerto_Serie.write(cadena)   
	
	# Si puerto serie que esta a la espera de que se escriba algo es > a 0
	if puerto_Serie.inWaiting() > 0:
		
		# La variable datos de tipo lista almacena lo que leemos del puerto serie
		datos = puerto_Serie.readline()
		
		# La variable dato_puerta recoje el dato de la posicion 7 de la lista datos
		dato_puerta=datos[7]
		
		# La variable dato_nivel recoje el dato de la posicion 17 de la lista datos hasta el final de la lista
		dato_nivel=datos[17:]
		
		# Creamos la variable dic de tipo diccionario con las claves "nivel", que manda el dato_nivel convertido en entero
		# y la clave "puerta", que manda el valor dato_puerta
		dic = {"nivel":int(dato_nivel) , "puerta":dato_puerta}

		return dic

		# Pequeño tiempo de espera
		time.sleep(0.1)   
		
		# Vuelvo a inicializar la variable datos a una lista vacia
		datos=[]
		

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
