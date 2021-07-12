import os
def menu():
	print("\t1-ROT13\n\t2-CESAR")
def decalage(p):
		if p>122:
			p=p-26
			f=p
			return f
		elif p<=122:
			f=p
			return f
texte = input(f'Entrer le text clair : \n[{"Kofra"}]>')
menu()
choix = (int)(input(f'[{"Kofra"}]>'))
if(choix==1):
	os.system("cls")
	print("-------ROT13-------")
	print("text clair : ",texte)
	#for i in texte:
	#	x=ord(i)
	#	if(x+13)>122:
	#		x=(x+13)-26
	#	print(chr(x))
	i=[ord(i)+13 for i in texte]
	x=[decalage(x) for x in i ]
	rot13=[chr(rot13) for rot13 in x]
	print("text chiffré : ",''.join(rot13))
elif(choix==2):
	os.system("cls")
	print("-------CHIFFRE DE CESAR-------")
	print("text clair : ",texte)
	cle = (int)(input('Entrer clé k : '))
	i=[ord(i)+cle for i in texte]
	x=[decalage(x) for x in i ]
	cesar=[chr(cesar) for cesar in x]
	print("text chiffré : ",''.join(cesar))