Students = {"Magentakale" : 38, "Marigold" : 60}
print(Students["Marigold"])
Students["Blue"] = 40
print(Students)

#Tuples
Names = ("Vanessa", "Leslie", "David", "Nelson", "Peter", "Lydia", "David")
print(Names)
print(len(Names))

Nametuple = ("Vanessa",) #NB: this is also a tuple
print(Nametuple)
#Tuples can have different data types (INT, Strings, Boolean)
Age = (30,40,27, 15,9,56,67)
Answertuple = ("true", "false", "true", "false", "false", "true")
print(Answertuple)
print(type(Answertuple))

Varietytuple= (30, "vanessa", "false", "male", 32)
print(Varietytuple)
print(type(Varietytuple))

#Conditions in python
#Oneway
age=60
if age >= 60:
    print("You are too old to work")

Name= "Vou"
if Name == "Jibo":
    print("Allow Access")
elif Name != "Jibo":
    print("Access Denied")
a=2
b=500
if a > b:
    print("a is greater than b")
elif b == a:
    print("b is equal to a")
else:
    print("a is less than b")
#Loops - Finite/Infinite

Food = ["Pawpaw", "Dodo", "Semo"]
for i in Food:
    print(i)
Fruits = {"Cashew":1, "Agbalumo":3, "Soursop":9}
for i in Fruits.items():
    print(i)

for i,j in Fruits.items():
    print(i,j)