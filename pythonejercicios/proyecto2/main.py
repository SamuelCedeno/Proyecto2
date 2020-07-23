from Modulo_1 import show_cruseros_info
from Modulo_1 import show_cruseros_buy
from Modulo_2 import clientes,clientesp,clientesv
from Modulo_3 import tour_sell
from Tour import Tour
from Modulo_4 import restaurant
from Modulo_5 import stats


def find_delete():
    keep=True
    while keep:

        des=input('''
        Seleccione que tipo de habitaciones desea ver

        1.Simples

        2.Premium

        3.VIP

        4.Salir

        :

        ''')
        if des=='1':
            for a,x in enumerate(clientes):
                print(f'------------{a+1}------------')
                print(x.show())
            ask=input("Desea desocupar una habitacion? y/n:")
            if ask=='y':
                sele=int(input('Marca el numero entre lineas para desocupar la habitacion:'))
                clientes.pop(sele-1)
                print("Habitacion desocupada con exito!")
            else:
                keep=True
        if des=='2':
            for a,x in enumerate(clientesp):
                print(f'------------{a+1}------------')
                print(x.show())
            ask=input("Desea desocupar una habitacion? y/n:")
            if ask=='y':
                sele=int(input('Marca el numero entre lineas para desocupar la habitacion:'))
                clientesp.pop(sele-1)
                print("Habitacion desocupada con exito!")
            else:
                keep=True
        if des=='3':
            for a,x in enumerate(clientesv):
                print(f'------------{a+1}------------')
                print(x.show())
            ask=input("Desea desocupar una habitacion? y/n:")
            if ask=='y':
                sele=int(input('Marca el numero entre lineas para desocupar la habitacion:'))
                clientesv.pop(sele-1)
                print("Habitacion desocupada con exito!")
            else:
                keep=True
        if des=='4':
            keep=False




def main():

    keep=True
    con=1
    inside=0
    gastos_cruce=0

    while keep:

        try:


            print('''





             _____                                  _____               _  _      _                         
            /  ___|                                /  __ \             (_)| |    | |                        
            \ `--.   __ _  _ __ ___    __ _  _ __  | /  \/  __ _  _ __  _ | |__  | |__    ___   __ _  _ __  
             `--. \ / _` || '_ ` _ \  / _` || '_ \ | |     / _` || '__|| || '_ \ | '_ \  / _ \ / _` || '_ \ 
            /\__/ /| (_| || | | | | || (_| || | | || \__/\| (_| || |   | || |_) || |_) ||  __/| (_| || | | |
            \____/  \__,_||_| |_| |_| \__,_||_| |_| \____/ \__,_||_|   |_||_.__/ |_.__/  \___| \__,_||_| |_|


            1.Ver informacion de cruceros

            2.Comprar boletos

            3.Buscar/Desocupar

            4.Comprar Tours

            5.Acceder a restaurant

            6.Estadisticas

            7.Salir

            ''')
            ask=input("Seleccione que desea hacer:")
            if ask=='1':
                show_cruseros_info()
            elif ask=='2':
                gastos_cruce+=show_cruseros_buy(con)
                con+=1
            elif ask=='3':
                find_delete()
            elif ask=='4':
                inside+=tour_sell(inside)
            elif ask=='5':
                restaurant()
            elif ask=='6':
                stats(inside, gastos_cruce)

            elif ask=='7':
                keep=False
        except:
            print("Valor incorrecto, intente de nuevo")


main()
