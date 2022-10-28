
# Bool
Happy = True
# String
Name = "Sithembiso"
# Number
Number = 44
# Float
he_has = 36.67

# Classes/Objects
# class firstClass:
#     __init__():
#             print(f"Hello {name}")




print("There was a man named : "+Name)
print("He was "+str(Number)+" year\'s old ")
print(f"Type of he_has is : {type(he_has)}")
print(f"Type of Number is : {type(Number)}")
print(f"Type of Name is : {type(Name)}")
print(f"Type of Happy is : {type(Happy)}")

phrase1 = "There WAs a man NAmed : "+Name
phrase2 = "He was "+str(Number)+" year\"s old "
phrase3 = f"Type of he_has is : {type(he_has)}"

print(phrase1.lower())
print(phrase1.capitalize())
print(phrase1.title())
print(phrase1.find("re"))
print(phrase1.replace("ere","a"))
print(phrase1.casefold())
print(phrase1.swapcase())
print(phrase1.__getitem__(0))
print(phrase1.__getitem__(len(phrase1)-(len(phrase1)-1)))
print(phrase1.__getitem__(len(phrase1)-(len(phrase1)-2)))
print(len(phrase1))
print(phrase1.isalpha())