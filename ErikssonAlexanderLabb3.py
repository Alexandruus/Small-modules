"""
Alexander Eriksson
Windows 10
"""
month = [] #Skapar en tom lista där vi kan lagra värden som användaren anger för varje dag.
def december(): #Funktion för att ta emot värden  för varje dag i december.
    lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11','12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    k = 0
    while True:
        try:
            user_input = input("Skriv in temp för" " "+ lista[k] + " " "December: ") #Indexerar listan, börjar med 0 så att rätt siffra visas som aktuellt datum när användaren ska mata in.
            temp = int(user_input)                                                   #Gör om user input till int.
            month.append(temp)                                                       #Lägger in värdet i [month].
            k = k + 1                                                                #K+1 för att få rätt index i nästa loop.
            if k == 31:                                                              #Returnar när 31 värden är inlagda i [month].
                return
        except ValueError:                                                           #För att se till att användare skriver in rätt värde.
            print("Vänligen skriv in ett heltal!")
            
def print_menu():                                                                    #Funktion för att printa grund menyn.
        print("")
        print("Måndagens högsta temperatur, skriv MAX ")
        print("Månadens lägsta temperatur, skriv MIN ")
        print("Månadens medeltemp, skriv MEDEL ")
        print("Välj dag genom att skriva DAG ")
        print("Avsluta med EXIT ")
        print("")


def input_command():                                                                #Funktion för att ta emot användarens val av ovan alternativ.
    user_input = input("Ange ditt val: ")
    return user_input

def main():                                                                         #Main funktionen.
    user_input = ""
    running = True                                                                  #While loop utförs medan förhållande är True.
    while running == True:
        print_menu()                                                                #Anropar print_menu.
        command = input_command()                                                   #anropar input_command.
        
        if command == "MAX":                                                        #Om användare skriver in "MAX".
            print(max(month))                                                       #Tar högsta värdet i [month].
            
        elif command == "MIN":                                                      #Om användare skriver in "MIN".
            print(min(month))                                                       #Tar lägsta värdet i [month].
            
        elif command == "MEDEL":                                                    #Om användare skriver in "MEDEL".
            medel = sum(month)                                                      #Tar sammanlagda summan i [month].
            medelvärde = medel / 31                                                 #Räknar ut medelvärdet.
            print("{0:2.2f}".format (medelvärde))                                   #Skriver ut medelvärde med två decimaler.

        elif command == "DAG":                                                      #Om användaren skriver in "DAG".
            K = 0
            while K==0:                                                             #While loop + Try&Except för att användare ska skriva in rätt värde.
                try:                                                                #Använder även en if/else för att användaren inte ska kunna skriva in
                    Dag=input("Ange Datum:")                                        #t.ex. 0 och ändå få ett indexvärde i listan..
                    Dagen=int(Dag)                                                    
                    if Dagen <= 31 and Dagen >= 1:                                  
                        Dagen= Dagen - 1                                            #Tar det värde som användare skriver in, sedan minus 1 så att det datum hen vill se är korrekt
                        print(month[Dagen])                                         #i förhållande till dess index i [month]. Skriver därefter ut [month] indexerat med det värde användare
                        K= K+1                                                      #skrivit in. K= K+1 för att hoppa ur loopen.

                    else:
                        print("Vänligen skriv in ett tal mellan 1-31!")
                except:
                    print("Vänligen skriv in ett tal mellan 1-31!")



                                                                            
        elif command == "EXIT":                                                     #Om användare skriver "EXIT".
            print("Ciao!")
            running = False                                                         #Running=False för att hoppa ur loopen.

december()                                                                          #Kör först december funktionen
main()                                                                              #och sedan main. 
