import pickle
import os
from msvcrt import getch
import getpass, sys

class room:
    def __init__(self, code, desc, cost, roomnos, availability):
        self.room_code = code               #int
        self.room_desc = desc               #string
        self.room_cost = cost               #float
        self.room_nos = roomnos                   #All the rooms for a particular room code
        self.room_availability = availability        #Availability of rooms true of false??

class admin:
    room_data = []
    username = 'user'
    password = 'user'
    
    def settings(self, username, password):
        self.username = username
        self.password = password

    def show_rooms(self):
        self.f=open("room_data.dat", "rb")
        self.f.seek(0)
        try:
            while True:                
                self.list=pickle.load(self.f)
                for i in self.list:
                    print('Room Code: ', i.room_code)
                    print('\tDescription: ', i.room_desc)
                    print('\tCost: ', i.room_cost)
                    print('\troom nos: ', i.room_nos)
                    print('\tavailability: ', i.room_availability)
        except:
            print('End of file reached')
        self.f.close()

    def set_room(self):     
        self.f=open('room_data.dat', 'ab+')
        n=int(input("Enter how many room types you want"))
        for i in range(0,n):
            print('\nEnter Room Details:')
            code = int(input('Enter Room Code in integers\n'))            
            desc = input('Enter Room Description\n')                         
            cost = float(input('Enter Cost of Room per night stay\n'))
            roomnos=eval(input("Enter room nos in list"))
            availability=[]
            
            for i in roomnos:
                availability.append(True)
            r = room(code, desc, cost, roomnos, availability)           
            self.room_data.append(r)
        pickle.dump(self.room_data, self.f)
        self.f.close()
        
    def change_room(self):
        code1 = int(input('Enter Room Code in which you want to make changes\n'))
        f = open("room_data.dat", "rb+")
        ft = open("temp.dat", "wb")
        f.seek(0)
        ft.seek(0)
        temp = []
        try:
            while True:
                room_data = pickle.load(f)
                for i in room_data:
                    if int(i.room_code) == code1:
                        print('\nEnter NEW Room Details:')            
                        desc = input('Enter Room Description\n')                         
                        cost = float(input('Enter Cost of Room per night stay\n'))
                        roomnos=eval(input("Enter room nos as list"))
                        avail = []
                        for i in roomnos:
                            avail.append(True)
                        r = room(int(code1), desc, cost, roomnos, avail)
                        temp.append(r)
                        for k in temp:
                            print(k.room_code, k.room_desc)
                    else:
                        temp.append(i)
        except:
            pass
        pickle.dump(temp, ft)
        ft.close()
        f.close()
        os.remove('room_data.dat')
        os.rename('temp.dat','room_data.dat')
        
    def delete_room(self):
        code1 = int(input('Enter Room Code you want to delete\n'))
        self.f = open("room_data.dat", "rb+")
        self.ft = open("temp.dat", "wb")
        self.f.seek(0)
        self.ft.seek(0)
        temp = []
        try:
            while True:
                self.room_data = pickle.load(self.f)
                for i in self.room_data:
                    if i.room_code == code1:
                        print('Room Data has been removed!')
                    else:
                        temp.append(i)
        except:
            pass
        pickle.dump(temp, self.ft)
        self.ft.close()
        self.f.close()
        os.remove('room_data.dat')
        os.rename('temp.dat','room_data.dat')
        
class Hotel: 
    room_no = 0      
    name = ''       
    days = 0         
    payment = 0      
    room_type = 0  
    
 
    def calpayment(self, admin):    
        self.f=open("room_data.dat", "rb+")
        try:
            while True:
                self.room_data=pickle.load(self.f)
        except:
            pass
        for i in self.room_data:
            if i.room_code == self.room_type:
                self.payment = (self.days) * i.room_cost

    def getdata(self, admin):
                   
        self.name=input('Enter name\n')                         
        self.days=int(input('Enter no. of days of stay\n'))
        print("Following room types are available:")
        admin.show_rooms()
        self.room_type=int(input("Enter Room Code"))
        
        self.calpayment(admin)   
        print('You have to pay Rs ', self.payment)
        
        print('Following rooms are available\n')
        #read rooms from file :P
        self.f=open("room_data.dat", "rb+")
        try:
            while True:
                self.room_data=pickle.load(self.f)
        except:
            pass
        for i in self.room_data:
            if i.room_code == self.room_type:
                for j in range(len(i.room_nos)):
                    #print(i.room_nos[j])
                    if i.room_availability[j] == True:
                        print(i.room_nos[j])
        self.f.close()

        f = open("room_data.dat", 'rb+')
        ft = open("temp", 'wb')
        self.room_no = int(input('\nEnter room no\n'))
        f.seek(0)
        ft.seek(0)
        temp =[]
        try:
            while True:
                room_data = pickle.load(f)
                for i in room_data:
                    if i.room_code == self.room_type:
                        index = 0
                        for j in i.room_nos:
                            index = index +1
                            if j == self.room_no:
                                i.room_availability[index-1] = False
                                temp.append(i)
                                break
                    else:
                        temp.append(i)
        except:
            pass
        pickle.dump(temp, ft)
        ft.close()
        f.close()
        os.remove("room_data.dat")
        os.rename("temp", "room_data.dat")

    def showdata(self):
        print('Room no = ', self.room_no)
        print('Name is', self.name)
        print('Days = ', self.days)
        print('Payment = ',self.payment)
        print('Room Type = ',self.room_type)

x=Hotel()
x1=Hotel()
admin = admin()

def create_room_data():
    n = int(input('Enter no. of Room Types you want to create'))
    for i in range(n):
        admin.set_room()
    code = int(input('Enter room code to add rooms'))
    n = int(input('Enter total no. of rooms'))
    room = []
    print('Enter room no.s')
    for i in range(n):
        r = int(input())
        room.append(r)
    admin.append(room,code)
    f = open('room_data.dat', 'ab+')
    pickle.dump(admin.room_data, f)
    f.close()



def read_rec():
    f=open("cust_data.dat", "rb")
    f.seek(0)
    try:
        while True:
            x=pickle.load(f)
            x.showdata(), print()
    except:
        print('End of file reached')
    f.close()

def write_rec():
    f = open("cust_data.dat", "ab+")
    ch='y'
    t = Hotel()
    while ch=='y':
        x.getdata(admin)
        t.room_no, t.name, t.days, t.payment, t.room_type = str(x.room_no), str(x.name), str(x.days), str(x.payment), str(x.room_type)
        print(type(t))
        print(t.room_no, t.name, t.days, t.payment, t.room_type)
        pickle.dump(t, f)
        ch=input('To write next data press y/n')
    f.close()

def Del_rec():
    ch='y'
    flag=0
    t = Hotel()
    f=open("cust_data.dat", 'rb+')
    ft=open("temp", 'wb')
    rno=input('Enter room no. for checkout.\n')   
    f.seek(0)
    ft.seek(0)
    try:
        while True:
            cust_data = pickle.load(f)
            if cust_data.room_no == rno:
                print('\nThe customer has checked out!\n')
                g = open("room_data.dat", 'rb+')
                gt = open("temp2", 'wb')
                g.seek(0)
                gt.seek(0)
                temp =[]
                try:
                    while True:
                        room_data = pickle.load(g)
                        for i in room_data:
                            print(i)
                            if i.room_code == int(cust_data.room_type):
                                index = 0
                                for j in i.room_nos:
                                    index = index +1
                                    if j == int(rno):
                                        i.room_availability[index-1] = True
                                        temp.append(i)
                                        break
                            else:
                                temp.append(i)
                except:
                    pass
                print(temp)
                pickle.dump(temp, gt)
                gt.close()
                g.close()
                os.remove("room_data.dat")
                os.rename("temp2", "room_data.dat")
            else:
                pickle.dump(cust_data,ft)
    except:
        pass
    ft.close()
    f.close()
    os.remove("cust_data.dat")
    os.rename("temp", "cust_data.dat")

def search_rec():
    f=open("cust_data.dat", 'rb')
    text=input('Enter any room no. whose record you want to search')
    flag=0
    f.seek(0)
    try:
        while True:
            x=pickle.load(f)
            if x.room_no==text:
                flag=1
                x.showdata()
                break
    except:
        print('End of file reached')
        if flag==0:
            print('No such record found')
    f.close()
    
def verify():
    choice = int(input('Are you a an \n\t 1.Admin \n\t 2.User\n'))
    if choice==1:
        password = input('Enter Password')
        '''
        try:
            print('Enter Password')
            password = getpass.getpass('Password :: ')
        except:
            pass'''
        if password == admin.password:
            ch='y'
            while ch=='y':        
                print('Welcome')
                print("Press 1 to WRITE a new ROOM record")
                print("Press 2 to SHOW (read) all room records")
                print("Press 3 to CHANGE a room record(s)")
                print("Press 4 to DELETE a room record")
                print("Press 5 to change accounts ADMIN/USER")
                print("Press 6 to EXIT")
                choice=int(input("->"))
                if choice==1:
                    admin.set_room()
                elif choice==2:
                    admin.show_rooms()
                elif choice==3:
                    admin.change_room()
                elif choice==4:
                    admin.delete_room()
                elif choice==5:
                    verify()                
                elif choice==6:
                    exit()
                else:
                    print("Wrong Choice!")
                    print("Please enter correct input.")
                    mainMenu()
                ch=input("Enter y to continue")
            
        else:
            print('Incorrect Password\nTry Again!!!')
    elif(choice == 2):
        mainMenu()


def mainMenu():
    print("Welcome to")
    print("\"HOTEL HOLIDAY INN\"")
    ch='y'
    while ch=='y':
        
        print("Press 1 to WRITE a new customer record")
        print("Press 2 to SHOW (read) all customer records")
        print("Press 3 to SEARCH a customer record")
        print("Press 4 to DELETE a customer record for CHECKOUT")
        print("Press 5 to change accounts ADMIN/USER")
        print("Press 6 to EXIT")
        choice=int(input("->"))

        if choice==1:
            write_rec()
        elif choice==2:
            read_rec()
        elif choice==3:
            search_rec()
        elif choice==4:
            Del_rec()
        elif choice==5:
            verify()                
        elif choice==6:
            exit()
        else:
            print("Wrong Choice!")
            print("Please enter correct input.")
            mainMenu()
        ch=input("Enter y to continue")

verify()
