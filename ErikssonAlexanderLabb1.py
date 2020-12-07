"""
Alexander Eriksson
Windows 10
"""


    
k = 0                       
Grader_Fahrenheit = 0
while k == 0:        #Skapar en while loop för att vra säker på att användaren kan skriva in siffror även efter en ValueError
    try:                                                                                   #Programmet försöker först på denna uträkning, om ValueError uppstår så hoppar den dit istället.
        Grader_Fahrenheit = int(input("Skriv grader Fahrenheit som du vill omvandla:"))    #Tar input av användare
        Grader_Celsius =(Grader_Fahrenheit - 32) * 5/9                                     #Formeln för omvandling
        print("Tempen är i grader Celsius:", "{0:2.2f}".format (Grader_Celsius))           #Print + format för att endast ha två decimaler
        k = 1                                                                              # Är K = 1 Så avbryts loopen och programmet eftersom användaren fått svar på frågan/omvandlningen.

    except ValueError:                                                                     #Om användaren skriver in bokstäver uppstår ValueError genom en try/except
        print("Vänligen skriv in numeriska siffror!")                       
        k = 0                                                                              # Om k = 0 så stannar användaren i loopen och får en ny chans att skriva in numemriska siffror
