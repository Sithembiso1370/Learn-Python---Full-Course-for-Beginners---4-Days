# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# defining a function called print_hi that takes in a parameter name
# def print_hi(name):
#     # Use a breakpoint in the co
#     # de line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# print_hi("Sthera")
# print("               .")
# print("              /|")
# print("             / |")
# print("            /  |")
# print("           /   |")
# print("          /    |")
# print("         /     |")
# print("        /      |")
# print("       /       |")
# print("      /________|")
# print("     /_________|")


# autogerate the above sequence
def createSymbolbetween(char1,char2,noOfSymbols,symbol):
    new_str = char1
    for x in range(noOfSymbols):
        new_str += symbol
    #
    return new_str + char2


for x in range(10):
     # print(x)
     if x == 0:
         print(" .")
     elif x == 9:
        print(createSymbolbetween("|",'\\',x,"_"))
     else:
         print(createSymbolbetween("|",'\\',x," "))



