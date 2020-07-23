from Tour import Tour

tour_ticket=[]
tour_people=[]

def tour_sell(inside):
    '''
    Funcion que deja elegir que tour desea seleccionar el cliente y luego calcula su precio

    Parametro: inside; un parametro que debe ser un int, este marca la cantidad de tickets comprado

    Retorna: insidex; es un valor int, indica cuanto dinero se ha hecho


    '''
    insidex=0

    while True:
        try:

            dni=input("Ingrese su DNI:")
            if not dni.isnumeric():
                raise NameError


            tour=input('''

            1.  ●Tour en el puerto

            2.  ●Degustación de comida local

            3.  ●Trotar por el pueblo/ciudad

            4.  ●Visita a lugares históricos

            5. Salir

            Seleccione el Tour que desea comprar:

            ''')

            if tour=='1':
                price=30
                name_tour='Tour en el puerto'
                capacity=10
                time='7 a.m'
                tours=Tour(dni,price,name_tour,capacity,time)
                people=int(input('Ingrese cuantas personas harán el tour:'))
                
                if people>4:
                    raise ValueError
                inside=people
                tours.tour_recip(people,inside)
                insidex+=people
                con=0
                while con<people:
                    tour_ticket.append(1)
                    tour_people.append(tours.tour_recip(people,inside))
                    con+=1
                    tour_db()
                    
            elif tour=='2':
                price=100
                name_tour='Degustación de comida local'
                capacity=100
                time='12 p.m'
                tours=Tour(dni,price,name_tour,capacity,time)
                people=int(input('Ingrese cuantas personas harán el tour:'))
                if people>2:
                    raise TabError
                inside=people
                tours.tour_recip(people,inside)
                insidex+=people
                con=0
                while con<people:
                    tour_ticket.append(1)
                    tour_people.append(tours.tour_recip(people,inside))
                    con+=1
                    tour_db()

            elif tour=='3':
                price=0
                name_tour='Tour en el puerto'
                capacity=0
                time='6 a.m'
                tours=Tour(dni,price,name_tour,capacity,time)
                people=int(input('Ingrese cuantas personas harán el tour:'))
                inside=people
                tours.tour_recip(people,inside)
                tour_people.append(tours.tour_recip(people,inside))
                insidex+=people
                tour_db()
            elif tour=='4':
                price=40
                name_tour='Visita a lugares históricos'
                capacity=15
                time='10 a.m'
                tours=Tour(dni,price,name_tour,capacity,time)
                people=int(input('Ingrese cuantas personas harán el tour:'))
                if people>4:
                    raise ValueError
                inside=people
                tours.tour_recip(people,inside)
                insidex+=people
                con=0
                while con<people:
                    tour_ticket.append(1)
                    tour_people.append(tours.tour_recip(people,inside))
                    con+=1
                    tour_db()
            elif tour=='5':
                break
        except ValueError:
            print("Este tour es para un maximo de grupos de 4 personas, intentelo de nuevo")
        except TabError:
            print("Este tour es para un maximo de grupos de 2 personas, intentelo de nuevo")
        except NameError:
            print('DNI erroneo, asegurate que sean caracteres numericos')
    return insidex

def tour_db():
    for x in tour_people:
        with open('Tour.txt','a') as f:
            f.write(f'{x}\n')