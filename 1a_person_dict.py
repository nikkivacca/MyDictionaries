from cgi import print_directory


person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

print(type(person["children"]))

print (type(person["pets"]))

# print child - "Betty"

child_name = person["children"][1]
print(child_name)

# print the pet name of the cat

cat_name = person["pets"]["cat"]
print(cat_name)

# use a for loop to print out all the children

for kid in person["children"]:
    print(kid)

# use a for loop to print out the type of pet and name of pet

for pets in person["pets"]:
    print(person['pets'][pets])
