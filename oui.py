		# b9t5.py

print("tu veux faire quoi sheguey ? ")

print("1 addition")

print("2 soustraction")

print("3 multiplication")

print("4 division")

choice=input()



print ("premier nombre")

a = int(input())

print ("deuxieme nombre")

b = int(input())

if choice=="1": 
	resultat=a+b

elif choice=="2":
	resultat=a-b

elif choice=="3":
	resultat=a*b

else:
	resultat=a/b

print(resultat)
