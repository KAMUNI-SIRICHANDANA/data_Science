# # class Rectangle:
# #     def __init__(self,l,b):    #init -> initializing the data
# #         self.l = l
# #         self.b = b
        
# #     def getlength(self):
# #         return self.l
# #     def getbreadth(self):
# #         return self.b
# #     def area(self):
# #         return self.l*self.b
# # a = Rectangle(10,10)
# # print(a.area())



# #
# # class Point:
# #     x=5
# #     y=10
# #     def __init__(self,x,y):
# #         self.x = x
# #         self.y = y
# #     def show(self):
# #         return self.x,self.y

# # p1 = Point(2,3)
# # print("2D Coordinates ",p1.show())
# # print("X coordinate: ",Point.x)
# # print("Y coordinate: ",Point.y)



# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def distance(self,oth_point):
#         return ((oth_point.x-self.x)**2+((oth_point.y-self.y)**2)**0.5)

# p1=Point(1,2)
# p2=Point(3,5)
# print(p1.distance(p2))




class Driver:

    def __init__(self,id,name,vehicle=None):
        self.name=name
        self.id = id
        self.history =[]
        self.location=None
        self.status = "Available"
    def getInfo(self):
        print(f'Name: {self.name}, Driver ID: {self.id}, Location: {self.location}, status:{self.status}')

    def setStatus(self,status):
        old_status = self.status
        self.status = status

        print(f'The status of Driver is changed from {old_status} --> {self.status}')
    
    def getHistory(self):
        print(self.history)

    def completeRide(self):
        self.setStatus("Available")

z1=Zone()


d1=Driver(1,"Uma")
d2=Driver(2,"Siri")
d3=Driver(3,"Kalyani")
d4=Driver(4,"gowri")

drivers = [d1,d2,d3,d4]

# for div in drivers:
#     div.getInfo()

#     print("----------------------------------------------")



c1=Car("HB 5967", "Hyundai","Aura")
c2 = Car("BV 5789","Toyota","Etios")


d1.setStatus("Lunch")
d1.getInfo() 
d1.setStatus("Busy")       
d1.getInfo()

u1=User(3,"Jennifer")
u2=USer(4,"Kryz")


z1.addCars([c1,c2])
z1.addDrivers([d1,d2,d3,d4])
z1.addUsers([u1,u2])
z1.getInfo()

r1= User(3,"Jennifer")
d1.acceptRide(r1)
d1.getInfo()
d1.getHisory()





class Zone:
    def __init__(self):
        self.drivers=[]
        self.cars=[]
        self.user=[]


    def addDrivers(self,drivers_list):
        self.drivers.append(drivers_list)
        print("Drivers are added to the zone")

    def addUSers(self,users_list):
        self.drivers.append(drivers_list)
        print("Drivers are added to the zone")



    def getInfo(self):
        print([i.plate for i in self.cars])
        print("--------------------------")
        print(self.drivers)
        print("--------------------------")
        print(self.users)


class Car:
    def __init__(self,plate,make,model):
        self.plate=[]
        self.make=make
        self.model=model
        self.fuel_percent=0.7
        self.capacity=4

class User:
    def __init__(self,id,name):
        self.name=name
        self.id = id
        self.history =[]
        self.location=None

    def requestRide(self,dist):
        return self.id


    def acceptRide(self,user,dist=20):
        if self.status!="Availavle":
            print("Status is not available")
        else:
            print("Ride has been started with {user.name}")
            
            self.history.append([self.name, f'Rider: {user.name}', f'Distance:' {dist}'])
                                 



                                 






    
