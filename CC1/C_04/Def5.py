########################
#   Kviečia funkcijas kurios randa nustatytus pasirinkimus
########################

import re

def capital_case_count(d):
    return len(re.findall('[A-Z]', d))

def lower_case_count(d):
    return len(re.findall('[a-z]', d))

def word_count(d):
    return len(d.split())

def number_count(d):
    return len(re.findall('[0-9]', d))

d = input("Iveskite tai kas bus suskaiciuota: ")


print(capital_case_count(d))
print(lower_case_count(d))
print(word_count(d))
print(number_count(d))