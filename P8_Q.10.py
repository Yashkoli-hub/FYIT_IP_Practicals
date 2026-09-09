dict1 = {
"A": 10,
"B": 20
}

dict2 = {
"B": 50,
"C": 30,
}

dict1.update(dict2)
print(dict1)

dict2.update(dict1)
print(dict2)
