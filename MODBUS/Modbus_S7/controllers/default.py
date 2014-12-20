# -*- coding: utf-8 -*-

# Importamos las librerias de modbus
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp

def index():
    
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))
      
# Funcion de lectura de PLC de entradas y salidas
def Lectura_PLC():

				    # host="192.168.1.10",
    master = modbus_tcp.TcpMaster(host="192.168.1.10",port=5000)  # Conexion modbus tcp con la ip del esclavo y puerto del esclavo
    
    lectura=master.execute(1,cst.READ_HOLDING_REGISTERS,0,16)
    
    dic = {"DATOS":lectura}

    return dic


# ESCRITURA DE SALIDAS
def Escribir_OUT():
                                  # host="192.168.1.10",
    master = modbus_tcp.TcpMaster(host="192.168.1.10",port=5000) 
    
    numero=int(request.vars.numero)
    
    if numero==0:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 8, output_value=1)
    if numero==1:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 8, output_value=0)
    
    if numero==2:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 9, output_value=1)
    if numero==3:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 9, output_value=0)
    
    if numero==4:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 10, output_value=1)
    if numero==5:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 10, output_value=0)
    
    if numero==6:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 11, output_value=1)
    if numero==7:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 11, output_value=0)
    
    if numero==8:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 12, output_value=1)
    if numero==9:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 12, output_value=0)
	
    if numero==10:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 13, output_value=1)
    if numero==11:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 13, output_value=0)
    
    if numero==12:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 14, output_value=1)
    if numero==13:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 14, output_value=0)
    
    if numero==14:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 15, output_value=1)
    if numero==15:
	master.execute(1, cst.WRITE_SINGLE_REGISTER, 15, output_value=0)
        
    #return numero

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

