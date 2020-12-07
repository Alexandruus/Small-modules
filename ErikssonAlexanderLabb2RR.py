"""
Alexander Eriksson
Windows 10
Restuppgift
"""
def Palindrom(User_Input):
	not_valid = "!\"#€%&/()=? :,'" # En sträng med ogiltiga tecken som skall tas bort
	User_Input = User_Input.lower() #Gör om samtliga karaktärer till små bokstäver

	i=0                           #Ger "i" värdet 0
	while i < len( not_valid ):   #Om antalet ogiltiga tecken är större än i(0) så fortsätter while loopen.
			User_Input = User_Input.replace( not_valid[i], "")  #Replacar ogiltiga tecken med 'ingenting'  
			i = i + 1     #För att avbryta/hoppa ur while loopen.

	User_Input_index = len(User_Input) - 1 #-1 för att få sista karaktären i ordet och använda det som index.
	Tom_Lista = [] #Skapar en tom lista för att stoppa in User_Input i.
	while User_Input_index >= 0: #Så länge ordet är lika med eller större än 0.
		Tom_Lista.append(User_Input[User_Input_index]) #Stoppar in en karaktär i taget i listan, efter vilket index som är valt.
		User_Input_index = User_Input_index - 1        #Med hjälp av While-loopen, tar en karaktär i taget tills alla är i listan.
	User_Input_reverse = "".join(Tom_Lista)                #Gör om till en sammanhängande sträng
	if User_Input == User_Input_reverse:                   #if-förhållande, om det bearbetade ordet är samma  
			return True                            #som original User_Input.
	else:
			return False
			

User_Input = input("Skriv in ditt ord eller mening:") #Frågar användare om input
if (Palindrom(User_Input)):                     #Stoppar in inputen i funktionen ovan
	print ("Det är en Palindrom!")          #Print om funktionen visar sig True
else:
	print ("Det är inte en Palindrom :(")  #Print om funktionen visar sig False


