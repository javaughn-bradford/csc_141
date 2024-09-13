#03_11_Intentional_Error

#03_10_Every_Function
List= ['Travel', 'Experience new foods', 'skydiving', "French"]
Lists=list
#My list: 
print(List)
#How many I have on my list? : 
print(len(List))
("\n")

#This is in alphaetical order 
print(sorted(List))
#Regular Order 
print(Lists)
#Reversed Order 
reverse= sorted(List).reverse
print(Lists)
#without Skydivng 
List.remove('skydiving')
print(List)
("\n")
#Inserting get dream car
List.insert(3,'Get dream car')
print(List)

#Error :
#THe error I had put was on line 14 and 17, in of "List", I've put "Lists" and added an s.
#The code knows my original list is spelled as "List" so anything else will get picked up as something different 
