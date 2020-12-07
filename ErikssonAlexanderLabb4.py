"""
Alexander Eriksson
Windows 10
"""
import tkinter
import tkinter.messagebox

root_window = tkinter.Tk()                                                            #Skapar huvudfönstret, text/info label och input. Dessa görs globala för att 
label_message = "Välkommen till temp. omvandlaren"                                    #kunna nås i övriga funktioner.
big_info_label = tkinter.Label(root_window, text = label_message, font = ("ubuntu", 16), \
                                   height=10, width = 50, bg = "#990000")
user_input = tkinter.Entry(root_window, width = 33)

def main():                                                                            #main()-funktion som innehåller GUI-objekten som krävs för programmet och
    create_root_window()                                                               #ser till att allting "loopar"/hålls igång när programet körs.

    create_big_label()
    create_input_box()
    create_buttons()

    tkinter.mainloop()

def create_root_window():                                                               #Huvudfönster + titel.
    root_window.geometry("620x500+700+200")
    root_window.title("Temperaturomvandlaren")



def create_big_label():                                                                 #Skapar/sätter ut den stora labeln.
    big_info_label.grid(row = 0, rowspan = 1, column = 0, columnspan = 3, pady = 4, padx = 8)


def create_input_box():                                                                 #Skapar/sätter ut input-rutan. 
    user_input.insert(0, "Skriv din temperatur i Fahrenheit här")
    user_input.grid(row = 2, rowspan = 2, column = 1, columnspan = 1, padx = 4)
                                                                
def create_buttons():                                                                    #Skapar/sätter ut de knappar vi ska ha
    celsius_button = tkinter.Button(root_window, text = "Beräkna Celsius", width = 12, command = converter)
    quit_button = tkinter.Button(root_window, text = "Avsluta", width = 12, command = avsluta)


    celsius_button.grid(row = 2, column = 0, pady = 20)
    quit_button.grid(row = 2, column = 2, pady = 20)

def get_feedback_string(choice_var):                                                    #Funktion för att hämta användarinputen.
    user_input_text = user_input.get()
    feedback_string = ""    
    if choice_var == 4:
        feedback_string = user_input_text
        
    return feedback_string
    
def converter():
        try:
            Fahrenheit = float(get_feedback_string(4))                            #Programmet försöker först på denna uträkning, om ValueError uppstår så hoppar den dit istället.
            Fahrenheit = (Fahrenheit - 32) * 5/9                                  #Själva beräkningen
            Celsius = str ("{0:2.2f}".format (Fahrenheit))                        #Gör om det till en sträng
            big_info_label.config(text = "Tempen är i grader Celsius:" + (Celsius)) #Redigerar big_info_label text.
            
            if Fahrenheit >0:                                                     #Beroende på om det blev plus, minus eller nollgradigt så ändrar vi färgen/bg.
                big_info_label.config(bg = "#5cd65c")              
                
            elif Fahrenheit <0:
                big_info_label.config(bg = "#ccffff")
                
                
            elif Fahrenheit == 0:
                big_info_label.config(bg="#ffffff")
                

        except ValueError:                                                              #Om användaren skriver in bokstäver uppstår ValueError genom en try/except
            big_info_label.config(bg="#ff0000")                                         #Visuell feedback i form av text & färg
            big_info_label.config(text = "Vänligen skriv in numeriska siffror! ")                 
                                                                                    


def avsluta():                                                                          #Avslutar programmet, "askyesno" för att dubbelkolla.
    if tkinter.messagebox.askyesno("Avsluta", "Är du säker på att du vill avsluta?"):
        root_window.destroy()


                                                                                        #Anrop till main()-funktionen så att programmet startar
if __name__ == "__main__":
    main()

















    
