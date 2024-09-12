#03_10_Every_Function
List= ['Travel', 'Experience new foods', 'skydiving', "French"]
#My list: 
print(List)
#How many I have on my list? : 
print(len(List))
("\n")

#This is in alphaetical order 
print(sorted(List))
#Regular Order 
print(List)
#Reversed Order 
reverse= sorted(List).reverse
print(List)
#without Skydivng 
List.remove('skydiving')
print(List)
("\n")
#Inserting get dream car
List.insert(3,'Get dream car')
print(List)
