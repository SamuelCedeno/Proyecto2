import matplotlib
from Modulo_2 import *
from Modulo_1 import cruceros_ticket
from People_Recip import People_Recip
from Modulo_3 import tour_ticket
from Modulo_4 import menu,menu_combo
from operator import attrgetter
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def promedio_cliente_gasto(inside, gastos_cruce):
    names = ['tour', 'promedio', 'ticket']
    values = [inside, (inside+gastos_cruce), gastos_cruce]

    plt.figure(figsize=(6,6))
    plt.bar(names, values)
    plt.savefig('myfig.png')

def clientes_sin_tour():
    
    total=len(clientes+clientesp+clientesv)
    sin_tour=total-len(tour_ticket)
    porcentaje=(sin_tour/total)*100
    
    names = ['Totales', 'porcentaje sin tour', 'sintour']
    values = [total, porcentaje, sin_tour]

    plt.figure(figsize=(9, 3))
    plt.bar(names, values)
    plt.savefig('myfig.png')

def money_stats():

    clientes_total=clientes+clientesp+clientesv

    for x in sorted(clientes_total,key=attrgetter('total'),reverse=True):
        if con==3:
            break
        else:
            print(x.show_recip())
            con+=1

def ships_stats():

    cruceros_ticket

    counter = 0
    num = lista[0] 
    
    for i in lista: 
        curr_frequency = lista.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 

    print(f'El crucero mas vendido es {num}')

def restaurantes_stats():
    menu
    menu_combo

    track=[]
    for key,value in menu.items():

        track.append(key)

    counter = 0
    num = track[0] 

    for i in track: 
        curr_frequency = track.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
    print(f'Producto mas vendido del restaurante:{num}')

    track1=[]
    for key,value in menu.items():

        track1.append(key)

    counter = 0
    num = track[0] 

    for i in track1: 
        curr_frequency = track1.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
    print(f'Combo mas vendido del restaurante:{num}')


def stats(inside, gastos_cruce):
    keep=True
    while keep:
        try:
            st=int(input('''

            Seleccione que desea ver

            1.Promedio de gastos del cliente

            2.Tickets de crucero

            3.Clientes que mas consume

            4.Barco mas vendido

            5.Productos del restaurante mas vendidos

            6.Salir

            :
            '''))

            if st==1:
                promedio_cliente_gasto(inside, gastos_cruce)
            elif st==2:
                clientes_sin_tour()
            elif st==3:
                money_stats()
            elif st==4:
                ships_stats()
            elif st==5:
                restaurantes_stats()
            elif st==6:
                keep=False
        except:
            print('Valor incorrecto, intente de nuevo')
            








        

