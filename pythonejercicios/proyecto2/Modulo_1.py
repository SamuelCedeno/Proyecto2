
import requests
from Modulo_2 import *

cruceros_ticket=[]

#Especificaciones de los barcos. Los clientes podran elegir el de su preferencia. 

def api_SamanCaribbean():

    url=f"https://saman-caribbean.vercel.app/api/cruise-ships"

    response=requests.request("GET",url)
    return response.json()

def show_cruseros_info():

    cruseros_name=api_SamanCaribbean()
    con=0
    number=1

    while con<4:
        print(number,cruseros_name[con]["name"])
        con+=1
        number+=1

    while True:
        try:
            options=int(input("Por favor seleccione el crucero del cual desea ver informacion:"))

            if options==1:
                print(f'''

                Nombre del barco:{cruseros_name[0]["name"]}

                Ruta del barco:{cruseros_name[0]["route"]}

                Fecha de salida:{cruseros_name[0]["departure"]}

                Costos de habitacion:{cruseros_name[0]["cost"]}

                Este crucero posee 3 pisos, uno por cada tipo habitacion

                ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                Piso 1: Se encuentran las habitaciones Simple van desde {cruseros_name[0]["rooms"]["simple"]} y poseee una capacidad max {cruseros_name[0]["capacity"]["simple"]} personas

                Piso 2: Se encuentran las habitaciones Premium van desde {cruseros_name[0]["rooms"]["premium"]} y poseee una capacidad max {cruseros_name[0]["capacity"]["premium"]} personas

                Piso 3: Se encuentran las habitaciones V.I.P van desde {cruseros_name[0]["rooms"]["vip"]} y poseee una capacidad max {cruseros_name[0]["capacity"]["vip"]} personas

                -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                ''')
                out=input("Desea salir? y/n:")
                if out == "y":
                    break
                else:
                    pass
            elif options==2:
                print(f'''

                Nombre del barco:{cruseros_name[1]["name"]}

                Ruta del barco:{cruseros_name[1]["route"]}

                Fecha de salida:{cruseros_name[1]["departure"]}

                Costos de habitacion:{cruseros_name[1]["cost"]}

                Este crucero posee 3 pisos, uno por cada tipo habitacion

                ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                Piso 1: Se encuentran las habitaciones Simple van desde {cruseros_name[1]["rooms"]["simple"]} y poseee una capacidad max {cruseros_name[1]["capacity"]["simple"]} personas

                Piso 2: Se encuentran las habitaciones Premium van desde {cruseros_name[1]["rooms"]["premium"]} y poseee una capacidad max {cruseros_name[1]["capacity"]["premium"]} personas

                Piso 3: Se encuentran las habitaciones V.I.P van desde {cruseros_name[1]["rooms"]["vip"]} y poseee una capacidad max {cruseros_name[1]["capacity"]["vip"]} personas

                -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                ''')
                out=input("Desea salir? y/n:")
                if out == "y":
                    break
                else:
                    pass
            elif options==3:
                print(f'''

                Nombre del barco:{cruseros_name[2]["name"]}

                Ruta del barco:{cruseros_name[2]["route"]}

                Fecha de salida:{cruseros_name[2]["departure"]}

                Costos de habitacion:{cruseros_name[2]["cost"]}

                Este crucero posee 3 pisos, uno por cada tipo habitacion

                ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                Piso 1: Se encuentran las habitaciones Simple van desde {cruseros_name[2]["rooms"]["simple"]} y poseee una capacidad max {cruseros_name[2]["capacity"]["simple"]} personas

                Piso 2: Se encuentran las habitaciones Premium van desde {cruseros_name[2]["rooms"]["premium"]} y poseee una capacidad max {cruseros_name[2]["capacity"]["premium"]} personas

                Piso 3: Se encuentran las habitaciones V.I.P van desde {cruseros_name[2]["rooms"]["vip"]} y poseee una capacidad max {cruseros_name[2]["capacity"]["vip"]} personas

                -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                ''')
                out=input("Desea salir? y/n:")
                if out == "y":
                    break
                else:
                    pass
            elif options==4:
                print(f'''

                Nombre del barco:{cruseros_name[3]["name"]}

                Ruta del barco:{cruseros_name[3]["route"]}

                Fecha de salida:{cruseros_name[3]["departure"]}

                Costos de habitacion:{cruseros_name[3]["cost"]}

                Este crucero posee 3 pisos, uno por cada tipo habitacion

                ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                Piso 1: Se encuentran las habitaciones Simple van desde {cruseros_name[3]["rooms"]["simple"]} y poseee una capacidad max {cruseros_name[3]["capacity"]["simple"]} personas

                Piso 2: Se encuentran las habitaciones Premium van desde {cruseros_name[3]["rooms"]["premium"]} y poseee una capacidad max {cruseros_name[3]["capacity"]["premium"]} personas

                Piso 3: Se encuentran las habitaciones V.I.P van desde {cruseros_name[3]["rooms"]["vip"]} y poseee una capacidad max {cruseros_name[3]["capacity"]["vip"]} personas

                -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                ''')
                out=input("Desea salir? y/n:")
                if out == "y":
                    break
                else:
                    pass
        except:
            print("Valor incorrecto, intentelo de nuevo")

#Recibe 'ide' como parametro, esto va a marcar una especie de ID para buscar el usuario mas tarde
def show_cruseros_buy(ide):


    cruseros_name=api_SamanCaribbean()
    con=0
    number=1
    gastos=0

    while con<4:
        print(number,cruseros_name[con]["name"])
        con+=1
        number+=1

    while True:
        try:
            options=int(input("Por favor seleccione el crucero del cual desea comprar un boleto:"))

            if options==1:
                print(f'''

                Nombre del barco:{cruseros_name[0]["name"]}

                Ruta del barco:{cruseros_name[0]["route"]}

                Fecha de salida:{cruseros_name[0]["departure"]}

                Costos de habitacion:{cruseros_name[0]["cost"]}

                Este crucero posee 3 pisos, uno por cada tipo habitacion

                ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                Piso 1: Se encuentran las habitaciones Simple van desde {cruseros_name[0]["rooms"]["simple"]} y poseee una capacidad max {cruseros_name[0]["capacity"]["simple"]} personas

                Piso 2: Se encuentran las habitaciones Premium van desde {cruseros_name[0]["rooms"]["premium"]} y poseee una capacidad max {cruseros_name[0]["capacity"]["premium"]} personas

                Piso 3: Se encuentran las habitaciones V.I.P van desde {cruseros_name[0]["rooms"]["vip"]} y poseee una capacidad max {cruseros_name[0]["capacity"]["vip"]} personas

                -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                ''')
                out=input("Presione 'b' para comprar un boleto en esta embarcacion, si desea seguir revisando otras opciones presione 'n':")
                if out == "b":
                    for x,r in enumerate(cruseros_name[0]["rooms"]):
                        print(x+1,r)
                    ask=input("Que habitacion desea comprar:")
                    if ask=='1':
                        gastos+=room_info_Simple(ide)
                        cruceros_ticket.append(cruseros_name[0]['name'])
                        break
                    elif ask=='2':
                        gastos+=room_info_Premium(ide)
                        cruceros_ticket.append(cruseros_name[0]['name'])
                        break
                    elif ask=='3':
                        gastos+=room_info_Vip(ide)
                        cruceros_ticket.append(cruseros_name[0]['name'])
                        break
            elif options==2:
                print(f'''

                Nombre del barco:{cruseros_name[1]["name"]}

                Ruta del barco:{cruseros_name[1]["route"]}

                Fecha de salida:{cruseros_name[1]["departure"]}

                Costos de habitacion:{cruseros_name[1]["cost"]}

                Este crucero posee 3 pisos, uno por cada tipo habitacion

                ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                Piso 1: Se encuentran las habitaciones Simple van desde {cruseros_name[1]["rooms"]["simple"]} y poseee una capacidad max {cruseros_name[1]["capacity"]["simple"]} personas

                Piso 2: Se encuentran las habitaciones Premium van desde {cruseros_name[1]["rooms"]["premium"]} y poseee una capacidad max {cruseros_name[1]["capacity"]["premium"]} personas

                Piso 3: Se encuentran las habitaciones V.I.P van desde {cruseros_name[1]["rooms"]["vip"]} y poseee una capacidad max {cruseros_name[1]["capacity"]["vip"]} personas

                -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                ''')
                out=input("Presione 'b' para comprar un boleto en esta embarcacion, si desea seguir revisando otras opciones presione 'n':")
                if out == "b":
                    for x,r in enumerate(cruseros_name[0]["rooms"]):
                        print(x+1,r)
                    ask=input("Que habitacion desea comprar:")
                    if ask=='1':
                        gastos+=room_info_Simple2(ide)
                        cruceros_ticket.append(cruseros_name[1]['name'])
                        break
                    elif ask=='2':
                        gastos+=room_info_Premium2(ide)
                        cruceros_ticket.append(cruseros_name[1]['name'])
                        break
                    elif ask=='3':
                        gastos+=room_info_Vip2(ide)
                        cruceros_ticket.append(cruseros_name[1]['name'])
                        break

            elif options==3:
                print(f'''

                Nombre del barco:{cruseros_name[2]["name"]}

                Ruta del barco:{cruseros_name[2]["route"]}

                Fecha de salida:{cruseros_name[2]["departure"]}

                Costos de habitacion:{cruseros_name[2]["cost"]}

                Este crucero posee 3 pisos, uno por cada tipo habitacion

                ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                Piso 1: Se encuentran las habitaciones Simple van desde {cruseros_name[2]["rooms"]["simple"]} y poseee una capacidad max {cruseros_name[2]["capacity"]["simple"]} personas

                Piso 2: Se encuentran las habitaciones Premium van desde {cruseros_name[2]["rooms"]["premium"]} y poseee una capacidad max {cruseros_name[2]["capacity"]["premium"]} personas

                Piso 3: Se encuentran las habitaciones V.I.P van desde {cruseros_name[2]["rooms"]["vip"]} y poseee una capacidad max {cruseros_name[2]["capacity"]["vip"]} personas

                -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                ''')
                out=input("Presione 'b' para comprar un boleto en esta embarcacion, si desea seguir revisando otras opciones presione 'n':")
                if out == "b":
                    for x,r in enumerate(cruseros_name[0]["rooms"]):
                        print(x+1,r)
                    ask=input("Que habitacion desea comprar:")
                    if ask=='1':
                        gastos+=room_info_Simple3(ide)
                        cruceros_ticket.append(cruseros_name[2]['name'])
                        break
                    elif ask=='2':
                        gastos+=room_info_Premium3(ide)
                        cruceros_ticket.append(cruseros_name[2]['name'])
                        break
                    elif ask=='3':
                        gastos+=room_info_Vip3(ide)
                        cruceros_ticket.append(cruseros_name[2]['name'])
                        break

            elif options==4:
                print(f'''

                Nombre del barco:{cruseros_name[3]["name"]}

                Ruta del barco:{cruseros_name[3]["route"]}

                Fecha de salida:{cruseros_name[3]["departure"]}

                Costos de habitacion:{cruseros_name[3]["cost"]}

                Este crucero posee 3 pisos, uno por cada tipo habitacion

                ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                Piso 1: Se encuentran las habitaciones Simple van desde {cruseros_name[3]["rooms"]["simple"]} y poseee una capacidad max {cruseros_name[3]["capacity"]["simple"]} personas

                Piso 2: Se encuentran las habitaciones Premium van desde {cruseros_name[3]["rooms"]["premium"]} y poseee una capacidad max {cruseros_name[3]["capacity"]["premium"]} personas

                Piso 3: Se encuentran las habitaciones V.I.P van desde {cruseros_name[3]["rooms"]["vip"]} y poseee una capacidad max {cruseros_name[3]["capacity"]["vip"]} personas

                -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                ''')
                out=input("Presione 'b' para comprar un boleto en esta embarcacion, si desea seguir revisando otras opciones presione 'n':")
                if out == "b":
                    for x,r in enumerate(cruseros_name[0]["rooms"]):
                        print(x+1,r)
                    ask=input("Que habitacion desea comprar:")
                    if ask=='1':
                        gastos+=room_info_Simple4(ide)
                        cruceros_ticket.append(cruseros_name[3]['name'])
                        break
                    elif ask=='2':
                        gastos+=room_info_Premium4(ide)
                        cruceros_ticket.append(cruseros_name[3]['name'])
                        break
                    elif ask=='3':
                        gastos+=room_info_Vip4(ide)
                        cruceros_ticket.append(cruseros_name[3]['name'])
                        break
        except:
            print("Valor incorrecto, intentelo de nuevo")
    return gastos

