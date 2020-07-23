from Modulo_1 import api_SamanCaribbean
from Restaurant import Restaurant

menu=dict()
menu_combo=dict()

def add_food(index):
    '''Funcion que agrega platillos a un diccionario
    
    Parametros: recibe un int, esto marca un index por todo el diccionario del API
    
    Retorna: retorna un int, es el total del producto agregado'''
    menu_price=0
    keep=True

    while keep:
        try:

            platillo=api_SamanCaribbean()
            for i,x in enumerate(platillo[index]['sells']):
                print(f'-----------{i+1}---------')
                print(f"{x['name']}-{x['price']}$")

            selection=int(input('Seleccione el producto deseado:'))

            if selection==1:
                name_food=platillo[index]['sells'][0]['name']
                price=platillo[index]['sells'][0]['price']
                menu[name_food]=price
                drink=price
                size_drink=input("Seleccione el tamaño de su bebida S/M/L:").upper()
                if size_drink=="S":
                    size_drink="S"
                elif size_drink=="M":
                    size_drink="M"
                elif size_drink=="L":
                    size_drink="L"
                else:
                    raise Exception
                pack_food='No'
                store=Restaurant(name_food,price,size_drink,pack_food)
                menu_price+=store.drink()
                
            elif selection==2:
                name_food=platillo[index]['sells'][1]['name']
                price=platillo[index]['sells'][1]['price']
                menu[name_food]=price
                drink=price
                pack_food=input("Desea un empaque para su comida Y/N:").upper()
                if pack_food=="Y":
                    pack_food="Y"
                elif pack_food=="N":
                    pack_food=="N"
                else:
                    raise Exception
                size_drink='No'
                store=Restaurant(name_food,price,size_drink,pack_food)
                store.food()
            elif selection==3:
                name_food=platillo[index]['sells'][2]['name']
                price=platillo[index]['sells'][2]['price']
                menu[name_food]=price
                drink=price
                pack_food=input("Desea un empaque para su comida Y/N:").upper()
                if pack_food=="Y":
                    pack_food="Y"
                elif pack_food=="N":
                    pack_food=="N"
                else:
                    raise Exception
                store=Restaurant(name_food,price,size_drink,pack_food)
                menu_price+=store.food()

            elif selection==4:
                name_food=platillo[index]['sells'][3]['name']
                price=platillo[index]['sells'][3]['price']
                menu[name_food]=price
                drink=price
                pack_food=input("Desea un empaque para su comida Y/N:").upper()
                if pack_food=="Y":
                    pack_food="Y"
                elif pack_food=="N":
                    pack_food=="N"
                else:
                    raise Exception
                size_drink=input("Seleccione el tamaño de su bebida S/M/L:").upper()
                if size_drink=="S":
                    size_drink="S"
                elif size_drink=="M":
                    size_drink="M"
                elif size_drink=="L":
                    size_drink="L"
                else:
                    raise Exception
                store=Restaurant(name_food,price,size_drink,pack_food)
                menu_price+=store.food_drink()

            elif selection==5:
                name_food=platillo[index]['sells'][4]['name']
                price=platillo[index]['sells'][4]['price']
                menu[name_food]=price
                drink=price
                size_drink=input("Seleccione el tamaño de su bebida S/M/L:").upper()
                if size_drink=="S":
                    size_drink="S"
                elif size_drink=="M":
                    size_drink="M"
                elif size_drink=="L":
                    size_drink="L"
                else:
                    raise Exception
                pack_food='No'
                store=Restaurant(name_food,price,size_drink,pack_food)
                menu_price+=store.drink()
            ask=input("Desea salir y/n:")
            if ask=='y':
                resta_db()
                keep=False
            elif ask=='n':
                keep=True
            else:
                raise Exception

        except:
            print("Valor erroneo, por favor intente de nuevo")

    return menu_price

def delete_product():
    '''Funcion que busca en el diccionario luego de serle introducido un input
    al encontrar una coincidencia este elimina el producto, caso contrario arroja un mensaje
    indicando que el producto no existe
    
    Parametos: ninguno
    
    Retorna: none'''

    for x in menu:
        print(x)
    
    dele=input("Escriba el nombre del producto a eliminar:")

    if dele in menu:

        menu.pop(dele)
        print("Producto eliminado con exito!")

    else:
        print("El producto no existe")

def delete_combo():
    '''Funcion que busca en el diccionario luego de serle introducido un input
    al encontrar una coincidencia este elimina el producto, caso contrario arroja un mensaje
    indicando que el producto no existe
    
    Parametos: ninguno
    
    Retorna: none'''
    for x in menu_combo:
        print(x)
    
    dele=input("Escriba el nombre del producto a eliminar:")

    if dele in menu_combo:

        menu_combo.pop(dele)
        print("Producto eliminado con exito!")

    else:
        print("El producto no existe")

def modify():
    '''Funcion que modifica un parametro introducido y lo agrega al menu
    
    Parametros: Ninguno
    
    Retorna: None'''

    for x in menu:
        print(x)
    
    dele=input("Escriba el nombre del producto a modificar:")

    if dele in menu:

        menu.pop(dele)
        dele=input("Introduzca el nuevo nombre del producto:")
        price=float(input("Introduzca el precio del profucto"))
        menu[dele]=[price]
        print("Producto modificado con exito!")

    else:
        print("El producto no existe")

def combos_menu(index):
    '''Funcion que agrega combos de platos a un diccionario
    
    Parametros: recibe un int, esto marca un index por todo el diccionario del API
    
    Retorna: retorna un int, es el total del producto agregado'''

    combo_price=0

    keep=True

    while keep:

        try:

            platillo=api_SamanCaribbean()
            for i,x in enumerate(platillo[index]['sells']):
                print(f'-----------{i+1}---------')
                print(f"{x['name']}-{x['price']}$")

            op1=int(input("Selecciona un articulo para el combo:"))
            op2=int(input("Selecciona un segundo articulo para el combo:"))
            namek='Combo del Mar'
            name_food=f'{platillo[index]["sells"][op1-1]["name"]} y {platillo[index]["sells"][op2-1]["name"]}'
            price=platillo[index]["sells"][op1-1]["price"]+platillo[index]["sells"][op2-1]["price"]
            size_drink=''
            pack_food=''
            menu_combo[name_food]=price
            combo=Restaurant(name_food,price,size_drink,pack_food)
            combo_price+=combo.kombos(namek)
            ask=input("Desea salir y/n:")
            if ask=='y':
                keep=False
            else:
                keep=True
        except:
            print('Valor erroneo, intente nuevo')

    return combo_price

def find_products():
    '''Funcion que busca productos ya sea combos o productos individuales 
    por un rango de precio introducido por un input
    
    Parametros:Ninguno
    
    Retorna:None'''

    while True:
        try:

            find=int(input('''

            1.Buscar productos 

            2.Buscar Combos

            :

            '''))

            if find==1:
                for x,b in menu.items():
                    rango=int(input('''

                    1.Precio mas alto

                    2.Precio medio

                    3.Precio bajo

                    :

                    '''))

                    if rango==1:
                        if b<10:
                            print(f'{x}---{b}')
                            break
                    elif rango ==2:
                        if b<40:
                            print(f'{x}---{b}')
                            break
                    elif rango==3:
                        if b>40:
                            print(f'{x}---{b}')
                            break
            elif find ==2:
                for x,b in menu.items():
                    rango=int(input('''

                    1.Precio mas alto

                    2.Precio medio

                    3.Precio bajo

                    :

                    '''))

                    if rango==1:
                        if b<30:
                            print(f'{x}---{b}')
                            break
                    elif rango ==2:
                        if b<60:
                            print(f'{x}---{b}')
                            break
                    elif rango==3:
                        if b>60:
                            print(f'{x}---{b}')
                            break
        except:
            print("Error, ha ingresado un valor incorrecto, por favor intente de nuevo")

def restaurant():

    keep=True
    cruseros_name=api_SamanCaribbean()

    while keep:
        try:
            ask=int(input('''
            
            Bienvenido

            Seleccione que desea hacer

            1.Agregar platos

            2.Eliminar productos del menu

            3.Modificar productos del menu

            4.Agregar combos al menu

            5.Eliminar combos del menu

            6.Buscar productos/combos

            7.Salir

            :
            
            '''))

            if ask==1:
                con=0
                number=1

                while con<4:
                    print(number,cruseros_name[con]["name"])
                    con+=1
                    number+=1
                pick=int(input("Elige un barco:"))
                if pick==1:
                    add_food(0)
                elif pick==2:
                    add_food(1)
                elif pick==3:
                    add_food(2)
                elif pick==4:
                    add_food(3)
                else:
                    raise Exception
            elif ask==2:
                delete_product()
            elif ask==3:
                modify()
            elif ask==4:
                con=0
                number=1

                while con<4:
                    print(number,cruseros_name[con]["name"])
                    con+=1
                    number+=1
                pick=int(input("Elige un barco:"))
                if pick==1:
                    combos_menu(0)
                elif pick==2:
                    combos_menu(1)
                elif pick==3:
                    combos_menu(2)
                elif pick==4:
                    combos_menu(3)
                else:
                    raise Exception
            elif ask==5:
                delete_combo()
            elif ask==6:
                find_products()
            elif ask==7:
                keep=False  
        except:
            print("Valor erroneo, por favor intentalo de nuevo")
             
def resta_db():
    for x,v in menu.items():
        with open('Restaurante.txt','a') as f:
            f.write(f'{x}----{v}$')



