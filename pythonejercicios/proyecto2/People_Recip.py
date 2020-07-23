
class People_Recip():

    def __init__(self,ide,name,dni,age,disability,refer,floor,letra_hall,room_selected,subtotal,discount,taxes,total):
        self.ide=ide
        self.name=name
        self.dni=dni
        self.age=age
        self.disability=disability
        self.refer=refer
        self.floor=floor
        self.letra_hall=letra_hall
        self.room_selected=room_selected
        self.subtotal=subtotal
        self.discount=discount
        self.taxes=taxes
        self.total=total

    def show_recip(self):

        if self.dni<1:
            descuento=self.discount=0
        elif self.dni==2:
            descuento=self.discount=0
        else:
            for i in range(3,(self.dni//2)+1):
                if self.dni%i==0:
                    descuento=self.discount=0
                    total=self.total-descuento
                    break
                else:
                    descuento=self.discount=0.1*self.total
                    total=self.total-descuento
        conta=0
        for x in range(1,self.dni):
            if self.dni%x==0:
                conta+=x
        if self.disability:
            descuento=self.discount=0.30*self.total
            total=self.total-descuento
        elif conta>self.dni:
            descuento=self.discount=0.15*self.total
            total=self.total-descuento
        else:
            descuento=self.discount=0
            total=self.total-descuento


        print(f'''
        
        Recibo {self.ide}

        Nombre:{self.name}
        D.N.I:{self.dni}
        Edad:{self.age}
        Discapacidad:{self.disability}
        Piso:{self.floor} Pasillo {self.letra_hall}
        Habitacion:{self.room_selected}
        Subtotal:{self.subtotal}
        Descuento:{descuento}
        Impuesto:{self.taxes}
        
        Total:{total}


        
        Referencia:{self.refer}


        
        ''')

        return total

        
    def show(self):

        return f'''
        
        Recibo {self.ide}

        Nombre:{self.name}
        D.N.I:{self.dni}
        Edad:{self.age}
        Discapacidad:{self.disability}
        Piso:{self.floor} Pasillo {self.letra_hall}
        Habitacion:{self.room_selected}
        Subtotal:{self.subtotal}
        Descuento:{self.discount}
        Impuesto:{self.taxes}
        
        Total:{self.total}

        Referencia:{self.refer}
        
        '''



