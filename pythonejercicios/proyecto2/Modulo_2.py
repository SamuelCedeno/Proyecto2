from Rooms import Rooms
from People_Recip import People_Recip
import requests
clientes=[]
clientesp=[]
clientesv=[]

#Multiples funciones para cada habitacion de cada crucero, se conecta con las respectivas clases
#People_Recip y Rooms, estas otorgan habitaciones dependiendo de los gustos del cliente y de la cantidad de estos 



def api():
    url=f"https://saman-caribbean.vercel.app/api/cruise-ships"

    responses=requests.request("GET",url)
    return responses.json()
def room_info_Simple(ide):
    '''
    Funcion que otorga habitaciones a los clientes

    Parametros: ide

    Retorna: gastos; es un valor int
    
    '''


    people=0
    letra_hall=["A"]
    floor=1
    n_room=[]
    capacity=2
    room_service=True
    view=False
    private_patry=False
    ide=ide
    gasto=0
 
    room_buy_si=api()

    roomSim=Rooms(people,n_room,capacity,room_service,view,private_patry)
    room=roomSim.room_buy_s1()

    con=1
    ide=ide
    while con<=room[1]:
        try:
            name=input("Introduza nombre y apellido:")
            age=int(input("Introduzca su edad:"))
            if age<0 or age>110:
                raise Exception("Edad incorrecta")
            elif age>65:

                third=input("Desea cambiar su habitacion por una Premium (Esta accion no tiene costo extra) y/n:")

                if third=='y':

                    dni=int(input("Introduzca su DNI:"))
                    if dni<3:
                        raise Exception
                    disa=input("Posee alguna discapacidad? y/n:")
                    if disa=="y":
                        disability=True
                    else:
                        disability=False
                    refer=input("Referencia del cliente:")

                    room_selected=room[0]
                    subtotal=room_buy_si[0]["cost"]["simple"]-(room_buy_si[0]["cost"]["simple"]*0.16)
                    discount=0
                    taxes=room_buy_si[0]["cost"]["simple"]-subtotal
                    total=room_buy_si[0]["cost"]["simple"]

                    data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)
                    clientesp.append(data)
                    gasto+=data.show_recip()
                    con+=1
                    ide+=1
                    data_base_simple()
            
            dni=int(input("Introduzca su DNI:"))
            if dni<3:
                raise Exception
            disa=input("Posee alguna discapacidad? y/n:")
            if disa=="y":
                disability=True
            else:
                disability=False
            refer=input("Referencia del cliente:")
    
            room_selected=room[0]
            subtotal=room_buy_si[0]["cost"]["simple"]-(room_buy_si[0]["cost"]["simple"]*0.16)
            discount=0
            taxes=room_buy_si[0]["cost"]["simple"]-subtotal
            total=room_buy_si[0]["cost"]["simple"]
            
            data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)
            clientes.append(data)
            gasto+=data.show_recip()
            con+=1
            ide+=1
            data_base_simple()
        except:
            print("Valor incorrecto, intente de nuevo")
    return gasto

def room_info_Premium(ide):
    '''
    Funcion que otorga habitaciones a los clientes

    Parametros: ide

    Retorna: gastos; es un valor int
    
    '''

    people=0
    letra_hall=["A"]
    floor=2
    n_room=[]
    capacity=4
    room_service=True
    view=True
    private_patry=False
    ide=ide
    gasto=0

    room_buy_si=api()
 

    roomSim=Rooms(people,n_room,capacity,room_service,view,private_patry)
    room=roomSim.room_buy_p1()

    con=1
    ide=ide
    while con<=room[1]:
        try:
            name=input("Introduza nombre y apellido:")
            age=int(input("Introduzca su edad:"))
            if age<0 or age>110:
                raise Exception("Edad incorrecta")
            dni=int(input("Introduzca su DNI:"))
            if dni<3:
                raise Exception
            disa=input("Posee alguna discapacidad? y/n:")
            if disa=="y":
                disability=True
            else:
                disability=False
            refer=input("Referencia del cliente:")
            room_selected=room[0]
            subtotal=room_buy_si[0]["cost"]["premium"]-(room_buy_si[0]["cost"]["premium"]*0.16)
            discount=0
            taxes=room_buy_si[0]["cost"]["premium"]-subtotal
            total=room_buy_si[0]["cost"]["premium"]
            
            data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)

            gasto+=data.show_recip()
            clientesp.append(data)

            con+=1
            ide+=1
            data_base_premium()
        except:
            print("Valor incorrecto, intente de nuevo")
    return gasto

def room_info_Vip(ide):
    '''
    Funcion que otorga habitaciones a los clientes

    Parametros: ide

    Retorna: gastos; es un valor int
    
    '''
    people=0
    letra_hall=["A"]
    floor=3
    n_room=[]
    capacity=8
    room_service=True
    view=True
    private_patry=False
    ide=ide
    gasto=0
  

    room_buy_si=api()


    roomSim=Rooms(people,n_room,capacity,room_service,view,private_patry)
    room=roomSim.room_buy_v1()

    con=1
    ide=ide
    while con<=room[1]:
        try:
            name=input("Introduza nombre y apellido:")
            age=int(input("Introduzca su edad:"))
            if age<0 or age>110:
                raise Exception("Edad incorrecta")
            dni=int(input("Introduzca su DNI:"))
            if dni<3:
                raise Exception
            disa=input("Posee alguna discapacidad? y/n:")
            if disa=="y":
                disability=True
            else:
                disability=False
            refer=input("Referencia del cliente:")
            room_selected=room[0]
            subtotal=room_buy_si[0]["cost"]["vip"]-(room_buy_si[0]["cost"]["vip"]*0.16)
            discount=0
            taxes=room_buy_si[0]["cost"]["vip"]-subtotal
            total=room_buy_si[0]["cost"]["vip"]
            
            data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)

            gasto+=data.show_recip()
            clientesv.append(data)

            con+=1
            ide+=1
            data_base_vip()
        except:
            print("Valor incorrecto, intente de nuevo")
    return gasto

def room_info_Simple2(ide):
    '''
    Funcion que otorga habitaciones a los clientes

    Parametros: ide

    Retorna: gastos; es un valor int
    
    '''
    people=0
    letra_hall=["A"]
    floor=1
    n_room=[]
    capacity=2
    room_service=True
    view=False
    private_patry=False
    ide=ide
    gasto=0


    room_buy_si=api()

    roomSim=Rooms(people,n_room,capacity,room_service,view,private_patry)
    room=roomSim.room_buy_s2()

    con=1
    ide=ide
    while con<=room[1]:
        try:
            name=input("Introduza nombre y apellido:")
            age=int(input("Introduzca su edad:"))
            if age<0 or age>110:
                raise Exception("Edad incorrecta")
            elif age>65:

                third=input("Desea cambiar su habitacion por una Premium (Esta accion no tiene costo extra) y/n:")

                if third=='y':

                    dni=int(input("Introduzca su DNI:"))
                    if dni<3:
                        raise Exception
                    disa=input("Posee alguna discapacidad? y/n:")
                    if disa=="y":
                        disability=True
                    else:
                        disability=False
                    refer=input("Referencia del cliente:")
                    room_selected=room[0]
                    subtotal=room_buy_si[1]["cost"]["simple"]-(room_buy_si[1]["cost"]["simple"]*0.16)
                    discount=0
                    taxes=room_buy_si[1]["cost"]["simple"]-subtotal
                    total=room_buy_si[1]["cost"]["simple"]

                    data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)
                    clientesp.append(data)
                    gasto+=data.show_recip()
                    con+=1
                    ide+=1
                    data_base_simple()
            dni=int(input("Introduzca su DNI:"))
            if dni<3:
                raise Exception
            disa=input("Posee alguna discapacidad? y/n:")
            if disa=="y":
                disability=True
            else:
                disability=False
            refer=input("Referencia del cliente:")
            room_selected=room[0]
            subtotal=room_buy_si[1]["cost"]["simple"]-(room_buy_si[1]["cost"]["simple"]*0.16)
            discount=0
            taxes=room_buy_si[1]["cost"]["simple"]-subtotal
            total=room_buy_si[1]["cost"]["simple"]
            
            data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)

            gasto+=data.show_recip()
            clientes.append(data)

            con+=1
            ide+=1
            data_base_simple()
        except:
            print("Valor incorrecto, intente de nuevo")
    return gasto

def room_info_Premium2(ide):
    '''
    Funcion que otorga habitaciones a los clientes

    Parametros: ide

    Retorna: gastos; es un valor int
    
    '''
    people=0
    letra_hall=["A"]
    floor=2
    n_room=[]
    capacity=4
    room_service=True
    view=True
    private_patry=False
    ide=ide
    gasto=0

    room_buy_si=api()
 

    roomSim=Rooms(people,n_room,capacity,room_service,view,private_patry)
    room=roomSim.room_buy_p2()

    con=1
    ide=ide
    while con<=room[1]:
        try:
            name=input("Introduza nombre y apellido:")
            age=int(input("Introduzca su edad:"))
            if age<0 or age>110:
                raise Exception("Edad incorrecta")
            dni=int(input("Introduzca su DNI:"))
            if dni<3:
                raise Exception
            disa=input("Posee alguna discapacidad? y/n:")
            if disa=="y":
                disability=True
            else:
                disability=False
            refer=input("Referencia del cliente:")
            room_selected=room[0]
            subtotal=room_buy_si[1]["cost"]["premium"]-(room_buy_si[1]["cost"]["premium"]*0.16)
            discount=0
            taxes=room_buy_si[1]["cost"]["premium"]-subtotal
            total=room_buy_si[1]["cost"]["premium"]
            
            data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)

            gasto+=data.show_recip()
            clientesp.append(data)

            con+=1
            ide+=1
            data_base_premium()
        except:
            print("Valor incorrecto, intente de nuevo")
    return gasto

def room_info_Vip2(ide):
    '''
    Funcion que otorga habitaciones a los clientes

    Parametros: ide

    Retorna: gastos; es un valor int
    
    '''

    people=0
    letra_hall=["A"]
    floor=3
    n_room=[]
    capacity=8
    room_service=True
    view=True
    private_patry=False
    ide=ide
    gasto=0

    room_buy_si=api()


    roomSim=Rooms(people,n_room,capacity,room_service,view,private_patry)
    room=roomSim.room_buy_v2()

    con=1
    ide=ide
    while con<=room[1]:
        try:
            name=input("Introduza nombre y apellido:")
            age=int(input("Introduzca su edad:"))
            if age<0 or age>110:
                raise Exception("Edad incorrecta")
            dni=int(input("Introduzca su DNI:"))
            if dni<3:
                raise Exception
            disa=input("Posee alguna discapacidad? y/n:")
            if disa=="y":
                disability=True
            else:
                disability=False
    
            room_selected=room[0]
            subtotal=room_buy_si[1]["cost"]["vip"]-(room_buy_si[1]["cost"]["vip"]*0.16)
            discount=0
            taxes=room_buy_si[1]["cost"]["vip"]-subtotal
            total=room_buy_si[1]["cost"]["vip"]
            refer=input("Referencia del cliente:")
            data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)

            gasto+=data.show_recip()
            clientesv.append(data)

            con+=1
            ide+=1
            data_base_vip()
        except:
            print("Valor incorrecto, intente de nuevo")
    return gasto

def room_info_Simple3(ide):
    '''
    Funcion que otorga habitaciones a los clientes

    Parametros: ide

    Retorna: gastos; es un valor int
    
    '''
    people=0
    letra_hall=["A"]
    floor=1
    n_room=[]
    capacity=3
    room_service=True
    view=False
    private_patry=False
    ide=ide
    gasto=0

    room_buy_si=api()

    roomSim=Rooms(people,n_room,capacity,room_service,view,private_patry)
    room=roomSim.room_buy_s3()

    con=1
    ide=ide
    while con<=room[1]:
        try:
            name=input("Introduza nombre y apellido:")
            age=int(input("Introduzca su edad:"))
            if age<0 or age>110:
                raise Exception("Edad incorrecta")
            elif age>65:

                third=input("Desea cambiar su habitacion por una Premium (Esta accion no tiene costo extra) y/n:")

                if third=='y':

                    dni=int(input("Introduzca su DNI:"))
                    if dni<3:
                        raise Exception
                    disa=input("Posee alguna discapacidad? y/n:")
                    if disa=="y":
                        disability=True
                    else:
                        disability=False
                    refer=input("Referencia del cliente:")
                    room_selected=room[0]
                    subtotal=room_buy_si[2]["cost"]["simple"]-(room_buy_si[2]["cost"]["simple"]*0.16)
                    discount=0
                    taxes=room_buy_si[2]["cost"]["simple"]-subtotal
                    total=room_buy_si[2]["cost"]["simple"]

                    data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)
                    clientesp.append(data)
                    gasto+=data.show_recip()
                    con+=1
                    ide+=1
                    data_base_simple()
            dni=int(input("Introduzca su DNI:"))
            if dni<3:
                raise Exception
            disa=input("Posee alguna discapacidad? y/n:")
            if disa=="y":
                disability=True
            else:
                disability=False
            refer=input("Referencia del cliente:")
            room_selected=room[0]
            subtotal=room_buy_si[2]["cost"]["simple"]-(room_buy_si[2]["cost"]["simple"]*0.16)
            discount=0
            taxes=room_buy_si[2]["cost"]["simple"]-subtotal
            total=room_buy_si[2]["cost"]["simple"]
            
            data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)

            gasto+=data.show_recip()
            clientes.append(data)

            con+=1
            ide+=ide
            data_base_simple()
        except:
            print("Valor incorrecto, intente de nuevo")
    return gasto

def room_info_Premium3(ide):
    '''
    Funcion que otorga habitaciones a los clientes

    Parametros: ide

    Retorna: gastos; es un valor int
    
    '''
    people=0
    letra_hall=["A"]
    floor=2
    n_room=[]
    capacity=5
    room_service=True
    view=True
    private_patry=False
    ide=ide
    gasto=0


    room_buy_si=api()
 

    roomSim=Rooms(people,n_room,capacity,room_service,view,private_patry)
    room=roomSim.room_buy_p3()

    con=1
    ide=ide
    while con<=room[1]:
        try:
            name=input("Introduza nombre y apellido:")
            age=int(input("Introduzca su edad:"))
            if age<0 or age>110:
                raise Exception("Edad incorrecta")
            dni=int(input("Introduzca su DNI:"))
            if dni<3:
                raise Exception
            disa=input("Posee alguna discapacidad? y/n:")
            if disa=="y":
                disability=True
            else:
                disability=False
            refer=input("Referencia del cliente:")
            room_selected=room[0]
            subtotal=room_buy_si[2]["cost"]["premium"]-(room_buy_si[2]["cost"]["premium"]*0.16)
            discount=0
            taxes=room_buy_si[2]["cost"]["premium"]-subtotal
            total=room_buy_si[2]["cost"]["premium"]
            
            data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)

            gasto+=data.show_recip()
            clientesp.append(data)

            con+=1
            ide+=1
            data_base_premium()
        except:
            print("Valor incorrecto, intente de nuevo")
    return gasto

def room_info_Vip3(ide):
    '''
    Funcion que otorga habitaciones a los clientes

    Parametros: ide

    Retorna: gastos; es un valor int
    
    '''

    people=0
    letra_hall=["A"]
    floor=3
    n_room=[]
    capacity=12
    room_service=True
    view=True
    private_patry=False
    ide=ide
    gasto=0

    room_buy_si=api()


    roomSim=Rooms(people,n_room,capacity,room_service,view,private_patry)
    room=roomSim.room_buy_v3()

    con=1
    ide=ide
    while con<=room[1]:
        try:
            name=input("Introduza nombre y apellido:")
            age=int(input("Introduzca su edad:"))
            if age<0 or age>110:
                raise Exception("Edad incorrecta")
            dni=int(input("Introduzca su DNI:"))
            if dni<3:
                raise Exception
            disa=input("Posee alguna discapacidad? y/n:")
            if disa=="y":
                disability=True
            else:
                disability=False
            refer=input("Referencia del cliente:")
            room_selected=room[0]
            subtotal=room_buy_si[2]["cost"]["vip"]-(room_buy_si[2]["cost"]["vip"]*0.16)
            discount=0
            taxes=room_buy_si[2]["cost"]["vip"]-subtotal
            total=room_buy_si[2]["cost"]["vip"]
            
            data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)

            gasto+=data.show_recip()
            clientesv.append(data)

            con+=1
            ide+=1
            data_base_vip()
        except:
            print("Valor incorrecto, intente de nuevo")
    return gasto

def room_info_Simple4(ide):
    '''
    Funcion que otorga habitaciones a los clientes

    Parametros: ide

    Retorna: gastos; es un valor int
    
    '''
    people=0
    letra_hall=["A"]
    floor=1
    n_room=[]
    capacity=3
    room_service=True
    view=False
    private_patry=False
    ide=ide
    gasto=0

    room_buy_si=api()

    roomSim=Rooms(people,n_room,capacity,room_service,view,private_patry)
    room=roomSim.room_buy_s4()

    con=1
    ide=ide
    while con<=room[1]:
        try:
            name=input("Introduza nombre y apellido:")
            age=int(input("Introduzca su edad:"))
            if age<0 or age>110:
                raise Exception("Edad incorrecta")
            elif age>65:

                third=input("Desea cambiar su habitacion por una Premium (Esta accion no tiene costo extra) y/n:")

                if third=='y':

                    dni=int(input("Introduzca su DNI:"))
                    if dni<3:
                        raise Exception
                    disa=input("Posee alguna discapacidad? y/n:")
                    if disa=="y":
                        disability=True
                    else:
                        disability=False
                    refer=input("Referencia del cliente:")
                    room_selected=room[0]
                    subtotal=room_buy_si[3]["cost"]["simple"]-(room_buy_si[3]["cost"]["simple"]*0.16)
                    discount=0
                    taxes=room_buy_si[3]["cost"]["simple"]-subtotal
                    total=room_buy_si[3]["cost"]["simple"]

                    data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)
                    clientesp.append(data)
                    gasto+=data.show_recip()
                    con+=1
                    ide+=1
                    data_base_simple()
            dni=int(input("Introduzca su DNI:"))
            if dni<3:
                raise Exception
            disa=input("Posee alguna discapacidad? y/n:")
            if disa=="y":
                disability=True
            else:
                disability=False
            refer=input("Referencia del cliente:")
            room_selected=room[0]
            subtotal=room_buy_si[3]["cost"]["simple"]-(room_buy_si[3]["cost"]["simple"]*0.16)
            discount=0
            taxes=room_buy_si[3]["cost"]["simple"]-subtotal
            total=room_buy_si[3]["cost"]["simple"]
            
            data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)

            gasto+=data.show_recip()
            clientes.append(data)

            con+=1
            ide+=1
            data_base_simple()
        except:
            print("Valor incorrecto, intente de nuevo")
    return gasto

def room_info_Premium4(ide):
    '''
    Funcion que otorga habitaciones a los clientes

    Parametros: ide

    Retorna: gastos; es un valor int
    
    '''
    people=0
    letra_hall=["A"]
    floor=2
    n_room=[]
    capacity=5
    room_service=True
    view=True
    private_patry=False
    ide=ide
    gasto=0

    room_buy_si=api()
 

    roomSim=Rooms(people,n_room,capacity,room_service,view,private_patry)
    room=roomSim.room_buy_p4()

    con=1
    ide=ide
    while con<=room[1]:
        try:
            name=input("Introduza nombre y apellido:")
            age=int(input("Introduzca su edad:"))
            if age<0 or age>110:
                raise Exception("Edad incorrecta")
            dni=int(input("Introduzca su DNI:"))
            if dni<3:
                raise Exception
            disa=input("Posee alguna discapacidad? y/n:")
            if disa=="y":
                disability=True
            else:
                disability=False
            refer=input("Referencia del cliente:")
            room_selected=room[0]
            subtotal=room_buy_si[3]["cost"]["premium"]-(room_buy_si[3]["cost"]["premium"]*0.16)
            discount=0
            taxes=room_buy_si[3]["cost"]["premium"]-subtotal
            total=room_buy_si[3]["cost"]["premium"]
            
            data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)

            gasto+=data.show_recip()
            clientesp.append(data)

            con+=1
            ide+=1
            data_base_premium()
        except:
            print("Valor incorrecto, intente de nuevo")
    return gasto

def room_info_Vip4(ide):

    '''
    Funcion que otorga habitaciones a los clientes

    Parametros: ide

    Retorna: gastos; es un valor int
    
    '''
    people=0
    letra_hall=["A"]
    floor=10
    n_room=[]
    capacity=8
    room_service=True
    view=True
    private_patry=False
    ide=ide
    gasto=0

    room_buy_si=api()


    roomSim=Rooms(people,n_room,capacity,room_service,view,private_patry)
    room=roomSim.room_buy_v4()

    con=1
    ide=ide
    while con<=room[1]:
        try:
            name=input("Introduza nombre y apellido:")
            age=int(input("Introduzca su edad:"))
            if age<0 or age>110:
                raise Exception("Edad incorrecta")
            dni=int(input("Introduzca su DNI:"))
            if dni<3:
                raise Exception
            disa=input("Posee alguna discapacidad? y/n:")
            if disa=="y":
                disability=True
            else:
                disability=False
            refer=input("Referencia del cliente:")
            room_selected=room[0]
            subtotal=room_buy_si[3]["cost"]["vip"]-(room_buy_si[3]["cost"]["vip"]*0.16)
            discount=0
            taxes=room_buy_si[3]["cost"]["vip"]-subtotal
            total=room_buy_si[3]["cost"]["vip"]
            
            data=People_Recip(ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total)

            gasto+=data.show_recip()
            clientesv.append(data)

            con+=1
            ide+=1
            data_base_vip()
        except:
            print("Valor incorrecto, intente de nuevo")
    return gasto

def data_base_simple():
    for x in clientes:
        with open('Rooms_Simple.txt','a') as f:
            f.write(x.show())

def data_base_premium():
    for x in clientesp:
        with open('Rooms_Premium.txt','a') as f:
            f.write(x.show())

def data_base_vip():

    for x in clientesv:
        with open('Rooms_VIP.txt','a') as f:
            f.write(x.show())
