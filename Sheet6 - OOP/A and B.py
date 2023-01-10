class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def GetData(self):
        return f"My name is: {self.__name},\n My age is: {self.__age}"
    def SetData(self, name, age):
        self.__name = name
        self.__age = age
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Student(Person):
    def __init__(self, name , age , type ):
        super().__init__(name, age)
        self.__type = type
    def GetData(self):
        string = super().GetData()
        return string + f"\nMy type is: {self.__type}"
    def SetData(self, name, age , type):
        super().SetData(name, age )
        self.__type = type
    #The following method is additional method you don't need to do it, it's just to make the concept stick in you mind
    def AmGoingTo(self, WhatAmGogingTo):
        if WhatAmGogingTo == 'Fail':
            print("Mohammed Atef will kill U")
        elif WhatAmGogingTo == 'Get Less than B+':
            print("محمد عاطف هيطلع يجري ورايا اعاااا ")
        else:
            print("Mohammed Atef will buy for you a pizza ❤")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Creating new objects from the classes to test the classes and the methods 
P1 = Person('Mohammed Atef' , "23")
print(P1.GetData())
S1 = Student('Atef' , '23', 'Male'
S1.SetData('Moahmmed' , 22  ,'Male')
print(S1.GetData())
S1.AmGoingTo('Get Less than B+')
