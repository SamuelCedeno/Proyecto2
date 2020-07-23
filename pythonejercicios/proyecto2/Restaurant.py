

class Restaurant():

    def __init__(self,name_food,price,size_drink,pack_food):
        self.name_food=name_food
        self.price=price
        self.size_drink=size_drink
        self.pack_food=pack_food

    
    def kombos(self,namek):

        name=self.name_food
        price=self.price
        tax=self.price*0.16
        total=price+tax

        print(f'''

        RESTAURANTE

        {namek}
        Combo:{name}

        Subtotal:{price}$

        Tax:{tax}$


        Total:{total}$
        
        ''')

        return total
        


    def food_drink(self):

        comida=self.price
        subtotal=comida
        tax=self.price*0.16
        total=subtotal+tax

        print(f'''
        
        Producto: {self.name_food} Empaque:{self.pack_food}
        Tamaño de la bebida:{self.size_drink}

        Subtotal: {subtotal}$
        IVA:+{tax}$

        Total:{total}$
        
        ''')

        return total 
    
    def food(self):

        comida=self.price
        subtotal=comida
        tax=self.price*0.16
        total=comida+tax

        print(f'''
        
        Producto: {self.name_food} Empaque:{self.pack_food}

        Subtotal: {subtotal}$
        IVA:+{tax}$

        Total:{total}$
        
        ''')

        return total

    def drink(self):

        bebida=self.price
        subtotal=bebida
        tax=self.price*0.16
        total=bebida+tax

        print(f'''
        
        Producto: {self.name_food} Tamaño:{self.size_drink}

        Subtotal: {subtotal}$
        IVA:+{tax}$

        Total:{total}$
        
        ''')

        return total