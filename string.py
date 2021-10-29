#Strings are one of the fundamental data type
#You can use either single or double quotes to create a string
#It holds ordered sequece of characters which means each character has a numbered position in the string
string1 = "Jagan Athkuri"
print(string1)
print(string1[2])
print(string1[-1])
#Obtaing a part of a string is called String Slicing
print(string1[2:8])
print(string1[3:-4])
#when we create string with quotes it is called String literal
#the quotes surrounding a string are called delimiters
#multiline String
string2 = "Blackboard"
#string concatenation
string3 = string1 + " " + string2
print(string3)
print(string3.replace("B","W"))
print(string3)
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno,price))
print(string3.strip("d"))