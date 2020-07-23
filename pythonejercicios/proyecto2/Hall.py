class Hall:
    def __init__(self,letra_hall,floor):
        self.letra_hall=letra_hall
        self.floor=floor

    def show_halla(self):

        print(f'''
        
        Piso: {self.floor}

        Pasillo: {self.letra_hall}
        
        ''')
