import json
i = 0

Dict={'Name':[],'hungry':[],'lunch':[],'age': [], 'animal':[], 'color':[], 'rather':[]}
while i < 2:
     #i < 2
     #i += 1
     Name = input("what is your Name?")
     Food = input("What's your favorite food?")
     Song = input("What is your favorite song?")
     age = input("how old are you?")
     animal = input("Fun Fact?")
     color = input("Favorite color?")
     rather = input("would you rather Read or Cry for 8 hrs? \na) read \nb) cry \n")
     Jasmine = input("Do you love Jasmine? Why?)
                     
     Dict["Name"].append(Name)
     Dict["Food"].append(hungry)
     Dict["Song"].append(lunch)
     Dict["age"].append(age)
     Dict["animal"].append(animal)
     Dict["color"].append(color)
     Dict["rather"].append(rather)
     Dict["Jasmine"].append(Jasmine)

     i = i + 1
     print(Dict)
#else:

Jsondict=json.dumps(Dict)
     #i = 0


f=open("Data.json",'w')
f.write(Jsondict)
f.close()






