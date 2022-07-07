integer1 = 5
float1 = 5.5
line = "I'm a line"
list1 = [integer1, float1, line]
dictionary = {1: "First", 2: "Second", 3: "Third", 4: list1}
logic_untrue = 3 < 0 

print("Use function type and give out variable type")

type_integer = type(integer1)
print("Integer is: ", type_integer)
print("Float is: ", type(float1))
print("Line is: ", type(line))
print("List is: ", type(list1))
print("Dictionary is: ", type(dictionary))
print("Logic is:", type(logic_untrue))

print("Using type to recognize integers in a list and add them")

list1_mix = [1, 2, 3, 4, "Five"]

addition = 0 
for elem in list1_mix:
    if type(elem) == int:
        addition += elem
print(addition)

