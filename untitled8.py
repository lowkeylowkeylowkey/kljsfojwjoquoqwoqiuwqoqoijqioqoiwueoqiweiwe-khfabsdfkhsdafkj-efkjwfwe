class Citizen:
    def __init__(self,name,age,dob,id_number):
        self.citizen_name = name
        self.citizen_age = age
        self.citizen_dob = dob
        self.citizen_id = id_number
        
    def add_citizen(self):
        print("Book Name: "+self.citizen_name)
        print("Book author: "+str(self.citizen_age))
        print("Book price: "+self.citizen_dob)
        print("Book was published in: "+self.citizen_id)
        print("Booked inserted")
        print("=================================")
        
        
citizen1 = Citizen("The Puzzling World of Winston Breen","Eric berlin","12.83$","2010")
citizen1.add_citizen()

citizen2 = Citizen("Spy School","Stuart Gibbs","20.31$","2003")
citizen2.add_citizen()



