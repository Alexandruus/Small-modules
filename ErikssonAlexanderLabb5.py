"""
Alexander Eriksson
Windows 10
"""


import tkinter                                                              #Importerar tKinter + messagebox
import tkinter.messagebox


root_window = tkinter.Tk()                                                  #Skapar huvudfönstret, text/info label och input. Dessa görs globala för att
label_message = "Skriv in den text du vill kontrollera nedanför!"           #kunna nås i andra funktioner
big_info_label = tkinter.Label(root_window, text = label_message, font = ("ubuntu", 16), \
                                   height=10, width = 50, bg = "#990000", fg = "white")
user_input = tkinter.Entry(root_window, width = 40)



def main():                                                                 #main()-funktion som innehåller GUI-objekten som krävs för programmet och
    create_root_window()                                                    #ser till att allting "loopar"/hålls igång när programet körs.

    create_big_label()
    create_input_box()
    create_buttons()

    tkinter.mainloop()


def create_root_window():                                                   #Huvudfönster + titel.
    root_window.geometry("620x500+700+200")
    root_window.title("Palindromdetektorn")

def create_big_label():                                                     #Skapar/sätter ut den stora labeln
    big_info_label.grid(row = 0, rowspan = 1, column = 0, columnspan = 3, pady = 4, padx = 8)


def create_input_box():                                                     #Skapar/sätter ut input-rutan. 
    user_input.insert(0, "Skriv ditt ord här")
    user_input.grid(row = 2, rowspan = 2, column = 1, columnspan = 1, padx = 4)


def create_buttons():                                                       #Skapar våra knappar och sätter ut de med hjälp av grid.
    evaluate_button = tkinter.Button(root_window, text = "Evaluera", width = 12, command = Palindrom)
    instructions_button = tkinter.Button(root_window, text = "Instruktioner", width = 12, command = instructions)
    save_button = tkinter.Button(root_window, text = "Spara", width = 12, command = save_to_file)
    quit_button = tkinter.Button(root_window, text = "Avsluta", width = 12, command = quit_game)

    evaluate_button.grid(row = 1, column = 0, pady = 5)
    instructions_button.grid(row = 2, column = 0, pady = 5)
    save_button.grid(row = 3, column = 0, pady = 5)
    quit_button.grid(row = 4, column = 0, pady = 5)


def get_feedback_string(choice_var):                                        #Funktion för att hämta användarinput. 
    user_input_text = user_input.get()
    feedback_string = ""

    if choice_var == 1:                                                     #if-sats för att hämta det användaren skriver in. Kopplad till palindrom() och save_to_file()
        feedback_string = user_input_text
        
    elif choice_var == 2:                                                   #elif-sats om användare trycker på instruktioner. 
        feedback_string = "Välkommen till Palindromdetektorn!\n" + \
                          "Skriv in din Palindrom i textrutan nedanför.\n" + \
                          "Tryck på Evaluera för att se om det är en Palindrom.\n" + \
                          "Tryck på Spara för att spara din Palindrom i en textfil.\n" +\
                          "Tryck på Avsluta för att avsluta Palindromdetektorn!" 
        
    return feedback_string                                                  #Returnar feedback_string 
    
def Palindrom():
    if (Palindrome_equation(get_feedback_string(1))):                       #if palindrome_equation funktionen är True så printar den ut att det är ett palindrom, else att det inte är...
        big_info_label.config(bg = "#5cd65c")
        big_info_label.config(text = "Det är en Palindrom")
    else:
        big_info_label.config(bg = "red")
        big_info_label.config(text = "Det är INTE en Palindrom")
    
def Palindrome_equation(user_input_text):                                   #Funktion för att se om det är ett palindrom.
            global user_palindrome                                          #Skapar user_palindrome samt gör den global så den går att använda i save_to_file funktionen.
            user_palindrome = get_feedback_string(1)                        #Hämtar feedback_string(1), = det användaren skrivit in
            not_valid = "!\"#€%&/()=? :,' "                                 #En sträng med ogiltiga tecken som skall tas bort
            user_palindrome = user_palindrome.lower()                       #Gör user_palindrome lower case.
            for i in not_valid:                                             #En for-sats där för varje gång "i" finns i not_valid så ersätts det med "ingenting".
                    user_palindrome = user_palindrome.replace(i, "")
                    if user_palindrome[::-1] == user_palindrome:            #Efter for-satsen är gjord så går user_palindrome till en enkel if/else-sats för att kolla om det är ett palindrom.
                            return True                                     #Och returnerar sedan värdet True om det är sant, och False om det inte är sant.

                    else:
                            return False


def instructions():                                                         
    feedback_string = get_feedback_string(2)                                #Hämtar feedback_string(2) och ändrar bg & fg-färg.
    big_info_label.config(bg = "blue")
    big_info_label.config(text = feedback_string, fg = "white")

def save_to_file():

    if (Palindrome_equation(get_feedback_string(1))):                       #Anropar Palindrome_equation. 
            try:                                                            #En try/except där vi försöker spara palindromen, och vid IOError ger användaren rimlig feedback.
                palindrom_file = open("palindrom.txt", "a")                 #Skapar text-fil, och appendar(a) user_palindrome. 
                palindrom_file.write( user_palindrome + "\n")               #Sparar vår gloabala variabel.
                palindrom_file.close()                                      #Stänger filen.                                  
                big_info_label.config(bg = "#5cd65c")                       #Ger användare feedback att vi lyckats spara palindromen.
                big_info_label.config(text = "Din Palindrom är sparad till textfil", fg = "white")
                
            except IOError:
                big_info_label.config(bg = "red")
                big_info_label.config(text = "Ett fel uppstod, kunde inte skriva till fil", fg = "white")
                
        
    else:
            big_info_label.config(bg = "red")
            big_info_label.config(text = "Hörredu! Du kan bara spara palindromer!", fg = "white")


def quit_game():                                                            #Funktionen för att avsluta + askyesno för att dubbelkolla. 
    if tkinter.messagebox.askyesno("Avsluta Palindromdetektorn", "Vill du verkligen avsluta?"):
        root_window.destroy()

                                                                            #Anrop till main()-funktionen så att programmet startar
if __name__ == "__main__":
    main()

















    
