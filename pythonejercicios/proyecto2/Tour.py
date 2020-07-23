class Tour():
    def __init__(self,dni,price,name_tour,capacity,time):
        self.dni=dni
        self.price=price
        self.name_tour=name_tour
        self.capacity=capacity
        self.time=time

    def tour_recip(self,people,inside):
        total=0
        con=1
        if inside==self.capacity:
            print("Los cupos del Tour estan llenos ")
        elif people>4:
            descuento=0
            total=0
        else:
            
            while con<=4:

                if people==4:
                    descuento=self.price*0.2
                    total=(self.price*people)-descuento
                    con+=1
                elif people==3:
                    descuento=self.price*0.1
                    total=(self.price*people)-descuento
                    con+=1
                elif people==1:
                    descuento=0
                    total=self.price*people
                    break
                elif people==2:
                    descuento=0
                    total=self.price*people
                    break

        print(f'''
        
        Recibo del Tour

        Nombre del tour:{self.name_tour}

        Peronsas inscritas:{people}

        Hora de incio:{self.time}

        Descuento si hay mas de 3 personas:{descuento}$

        Total:{total}$
        
        ''')
        return f'''
        
        Recibo del Tour

        Nombre del tour:{self.name_tour}

        Peronsas inscritas:{people}

        Hora de incio:{self.time}

        Descuento si hay mas de 3 personas:{descuento}$

        Total:{total}$
        
        '''

                

                




