from Hall import Hall
import random

r_data=[]
class Rooms(Hall):

    def __init__(self,people,n_room,capacity,room_service,view,private_party):
        self.people=people
        self.n_room=[]
        self.capacity=capacity
        self.room_service=room_service
        self.view=view
        self.private_party=private_party


    def room_buy_s1(self):

        keep=True

        while keep:
            try:
                ask=1
                if ask==1:
                    self.people=int(input("Cuantas personas viajan:"))

                    if self.people==1 or self.people==2:
                        hab=[[4,5,6],
                            [7,8,9]]
                        print(f"Las habitaciones disponibles son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        give=True
                        while give:
                            resulthab=random.choice(habselect)
                            if resulthab in self.n_room:
                                give=True
                            else:
                                self.n_room.append(resulthab)
                                give=False
                    if self.people>2:
                        hab=[[4,5,6],
                            [7,8,9]]
                        print(f"Las habitaciones son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        con=0
                        division=(self.people/2)+0.1

                        while con<round(division):

                            resulthab=random.choice(habselect)
  
                            if resulthab in r_data:
                                con+=0
                            elif resulthab not in r_data:
                                self.n_room.append(resulthab)
                                r_data.append(resulthab)
                                con+=1
                            else:
                                print("Ho hay habitaciones disponibles")

                    keep=False


            except:
                print("Error, intente de nuevo")
        return self.n_room,self.people

    def room_buy_s2(self):


        keep=True

        while keep:
            try:
                ask=1
                if ask==1:
                    self.people=int(input("Cuantas personas viajan:"))

                    if self.people==1 or self.people==2:
                        hab=[[6,7,8],
                            [9,10]]
                        print(f"Las habitaciones disponibles son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        give=True
                        while give:
                            resulthab=random.choice(habselect)
                            if resulthab in self.n_room:
                                give=True
                            else:
                                self.n_room.append(resulthab)
                                give=False
                    if self.people>2:
                        hab=[[6,7,8],
                            [9,10]]
                        print(f"Las habitaciones son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        con=0
                        division=(self.people/2)+0.1

                        while con<round(division):

                            resulthab=random.choice(habselect)
  
                            if resulthab in r_data:
                                con+=0
                            elif resulthab not in r_data:
                                self.n_room.append(resulthab)
                                r_data.append(resulthab)
                                con+=1
                            else:
                                print("Ho hay habitaciones disponibles")

                    keep=False


            except:
                print("Error, intente de nuevo")
        return self.n_room,self.people

    def room_buy_s3(self):


        keep=True

        while keep:
            try:
                ask=1
                if ask==1:
                    self.people=int(input("Cuantas personas viajan:"))

                    if self.people==1 or self.people==3:
                        hab=[[6,7,8],
                            [8]]
                        print(f"Las habitaciones disponibles son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        give=True
                        while give:
                            resulthab=random.choice(habselect)
                            if resulthab in self.n_room:
                                give=True
                            else:
                                self.n_room.append(resulthab)
                                give=False
                    if self.people>3:
                        hab=[[6,7],
                            [8]]
                        print(f"Las habitaciones son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        con=0
                        division=(self.people/3)+0.2

                        while con<round(division):

                            resulthab=random.choice(habselect)
  
                            if resulthab in r_data:
                                con+=0
                            elif resulthab not in r_data:
                                self.n_room.append(resulthab)
                                r_data.append(resulthab)
                                con+=1
                            else:
                                print("No hay habitaciones disponibles")

                    keep=False


            except:
                print("Error, intente de nuevo")
        return self.n_room,self.people

    def room_buy_s4(self):


        keep=True

        while keep:
            try:
                ask=1
                if ask==1:
                    self.people=int(input("Cuantas personas viajan:"))

                    if self.people==1 or self.people==3:
                        hab=[[4,5,6],
                            [7,8,9],
                            [10,11,12]]
                        print(f"Las habitaciones disponibles son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        give=True
                        while give:
                            resulthab=random.choice(habselect)
                            if resulthab in self.n_room:
                                give=True
                            else:
                                self.n_room.append(resulthab)
                                give=False
                    if self.people>3:
                        hab=[[4,5,6],
                            [7,8,9],
                            [10,11,12]]
                        print(f"Las habitaciones son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        con=0
                        division=(self.people/3)+0.2

                        while con<round(division):

                            resulthab=random.choice(habselect)
  
                            if resulthab in r_data:
                                con+=0
                            elif resulthab not in r_data:
                                self.n_room.append(resulthab)
                                r_data.append(resulthab)
                                con+=1
                            else:
                                print("Ho hay habitaciones disponibles")

                    keep=False


            except:
                print("Error, intente de nuevo")
        return self.n_room,self.people

    def room_buy_p1(self):
        keep=True

        while keep:
            try:
                ask=2
                if ask==2:
                    self.people=int(input("Cuantas personas viajan:"))

                    if self.people==1 or self.people<=4:
                        hab=[[3,4,5],
                            [6,7,8]]
                        print(f"Las habitaciones disponibles son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        give=True
                        while give:
                            resulthab=random.choice(habselect)
                            if resulthab in self.n_room:
                                give=True
                            else:
                                self.n_room.append(resulthab)
                                give=False
                    if self.people>4:
                        hab=[[3,4,5],
                            [6,7,8]]
                        print(f"Las habitaciones son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        con=0
                        division=(self.people/4)+0.3

                        while con<round(division):

                            resulthab=random.choice(habselect)
  
                            if resulthab in r_data:
                                con+=0
                            elif resulthab not in r_data:
                                self.n_room.append(resulthab)
                                r_data.append(resulthab)
                                con+=1
                            else:
                                print("Ho hay habitaciones disponibles")

                    keep=False


            except:
                print("Error, intente de nuevo")
        return self.n_room,self.people

    def room_buy_p2(self):
        keep=True

        while keep:
            try:
                ask=2
                if ask==2:
                    self.people=int(input("Cuantas personas viajan:"))

                    if self.people==1 or self.people<=4:
                        hab=[[4,5],
                            [6,7,8]]
                        print(f"Las habitaciones disponibles son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        give=True
                        while give:
                            resulthab=random.choice(habselect)
                            if resulthab in self.n_room:
                                give=True
                            else:
                                self.n_room.append(resulthab)
                                give=False
                    if self.people>4:
                        hab=[[4,5],
                            [6,7,8]]
                        print(f"Las habitaciones son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        con=0
                        division=(self.people/4)+0.3

                        while con<round(division):

                            resulthab=random.choice(habselect)
  
                            if resulthab in r_data:
                                con+=0
                            elif resulthab not in r_data:
                                self.n_room.append(resulthab)
                                r_data.append(resulthab)
                                con+=1
                            else:
                                print("Ho hay habitaciones disponibles")

                    keep=False


            except:
                print("Error, intente de nuevo")
        return self.n_room,self.people

    def room_buy_p3(self):
        keep=True

        while keep:
            try:
                ask=2
                if ask==2:
                    self.people=int(input("Cuantas personas viajan:"))

                    if self.people==1 or self.people<=5:
                        hab=[[4,5],
                            [6,7,8]]
                        print(f"Las habitaciones disponibles son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        give=True
                        while give:
                            resulthab=random.choice(habselect)
                            if resulthab in self.n_room:
                                give=True
                            else:
                                self.n_room.append(resulthab)
                                give=False
                    if self.people>5:
                        hab=[[4,5],
                            [6,7,8]]
                        print(f"Las habitaciones son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        con=0
                        division=(self.people/5)+0.4

                        while con<round(division):

                            resulthab=random.choice(habselect)
  
                            if resulthab in r_data:
                                con+=0
                            elif resulthab not in r_data:
                                self.n_room.append(resulthab)
                                r_data.append(resulthab)
                                con+=1
                            else:
                                print("Ho hay habitaciones disponibles")

                    keep=False


            except:
                print("Error, intente de nuevo")
        return self.n_room,self.people

    def room_buy_p4(self):
        keep=True

        while keep:
            try:
                ask=2
                if ask==2:
                    self.people=int(input("Cuantas personas viajan:"))

                    if self.people==1 or self.people<=5:
                        hab=[[4,5],
                            [6,7,8]]
                        print(f"Las habitaciones disponibles son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        give=True
                        while give:
                            resulthab=random.choice(habselect)
                            if resulthab in self.n_room:
                                give=True
                            else:
                                self.n_room.append(resulthab)
                                give=False
                    if self.people>5:
                        hab=[[4,5],
                            [6,7,8]]
                        print(f"Las habitaciones son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        con=0
                        division=(self.people/5)+0.4

                        while con<round(division):

                            resulthab=random.choice(habselect)
  
                            if resulthab in r_data:
                                con+=0
                            elif resulthab not in r_data:
                                self.n_room.append(resulthab)
                                r_data.append(resulthab)
                                con+=1
                            else:
                                print("Ho hay habitaciones disponibles")

                    keep=False


            except:
                print("Error, intente de nuevo")
        return self.n_room,self.people

    def room_buy_v1(self):


        keep=True

        while keep:
            try:
                ask=3
                if ask==3:
                    self.people=int(input("Cuantas personas viajan:"))

                    if self.people==1 or self.people<=8:
                        hab=[[1,2,3],
                            [4,5,6]]
                        print(f"Las habitaciones disponibles son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        give=True
                        while give:
                            resulthab=random.choice(habselect)
                            if resulthab in self.n_room:
                                give=True
                            else:
                                self.n_room.append(resulthab)
                                give=False
                    if self.people>8:
                        hab=[[1,2,3],
                            [4,5,6]]
                        print(f"Las habitaciones son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        con=0
                        division=(self.people/8)+0.4

                        while con<round(division):

                            resulthab=random.choice(habselect)
  
                            if resulthab in r_data:
                                con+=0
                            elif resulthab not in r_data:
                                self.n_room.append(resulthab)
                                r_data.append(resulthab)
                                con+=1
                            else:
                                print("Ho hay habitaciones disponibles")

                    keep=False


            except:
                print("Error, intente de nuevo")
        return self.n_room,self.people

    def room_buy_v2(self):



        keep=True

        while keep:
            try:
                ask=3
                if ask==3:
                    self.people=int(input("Cuantas personas viajan:"))

                    if self.people==1 or self.people<=8:
                        hab=[[1,2],
                            [3,4]]
                        print(f"Las habitaciones disponibles son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        give=True
                        while give:
                            resulthab=random.choice(habselect)
                            if resulthab in self.n_room:
                                give=True
                            else:
                                self.n_room.append(resulthab)
                                give=False
                    if self.people>8:
                        hab=[[1,2],
                            [3,4]]
                        print(f"Las habitaciones son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        con=0
                        division=(self.people/8)+0.4

                        while con<round(division):

                            resulthab=random.choice(habselect)
  
                            if resulthab in r_data:
                                con+=0
                            elif resulthab not in r_data:
                                self.n_room.append(resulthab)
                                r_data.append(resulthab)
                                con+=1
                            else:
                                print("Ho hay habitaciones disponibles")

                    keep=False


            except:
                print("Error, intente de nuevo")
        return self.n_room,self.people

    def room_buy_v3(self):



        keep=True

        while keep:
            try:
                ask=3
                if ask==3:
                    self.people=int(input("Cuantas personas viajan:"))

                    if self.people==1 or self.people<=12:
                        hab=[[1,2],
                            [3,4]]
                        print(f"Las habitaciones disponibles son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        give=True
                        while give:
                            resulthab=random.choice(habselect)
                            if resulthab in self.n_room:
                                give=True
                            else:
                                self.n_room.append(resulthab)
                                give=False
                    if self.people>12:
                        hab=[[1,2],
                            [3,4]]
                        print(f"Las habitaciones son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        con=0
                        division=(self.people/12)+0.42

                        while con<round(division):

                            resulthab=random.choice(habselect)
  
                            if resulthab in r_data:
                                con+=0
                            elif resulthab not in r_data:
                                self.n_room.append(resulthab)
                                r_data.append(resulthab)
                                con+=1
                            else:
                                print("Ho hay habitaciones disponibles")

                    keep=False


            except:
                print("Error, intente de nuevo")
        return self.n_room,self.people

    def room_buy_v4(self):



        keep=True

        while keep:
            try:
                ask=3
                if ask==3:
                    self.people=int(input("Cuantas personas viajan:"))

                    if self.people==1 or self.people<=10:
                        hab=[[1,2],
                            [3,4]]
                        print(f"Las habitaciones disponibles son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        give=True
                        while give:
                            resulthab=random.choice(habselect)
                            if resulthab in self.n_room:
                                give=True
                            else:
                                self.n_room.append(resulthab)
                                give=False
                    if self.people>10:
                        hab=[[1,2],
                            [3,4]]
                        print(f"Las habitaciones son: {hab}")
                        habselect=[]
                        for a in hab:
                            for x in a:
                                habselect.append(x)
                        con=0
                        division=(self.people/10)+0.41

                        while con<round(division):

                            resulthab=random.choice(habselect)
  
                            if resulthab in r_data:
                                con+=0
                            elif resulthab not in r_data:
                                self.n_room.append(resulthab)
                                r_data.append(resulthab)
                                con+=1
                            else:
                                print("Ho hay habitaciones disponibles")

                    keep=False


            except:
                print("Error, intente de nuevo")
        return self.n_room,self.people


