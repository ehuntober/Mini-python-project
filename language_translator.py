
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Translator")
root.geometry("500x500")
root.config(bg='blue')


lab_txt = Label(root, text = "Translator", font=("Time New Roman",40,"bold"))
lab_txt.place(x=100, y= 40, height = 50, width = 300)

frame = Frame(root).pack(side = BOTTOM)

lab_txt = Label(root, text = "Source Text", font=("Time New Roman",20,"bold"),fg="BLACK")
lab_txt.place(x=100, y=100, height=20, width = 300)

sor_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap= WORD)
sor_txt.place(x=10,y=130,height =200, width= 480)


list_text= [1,2,3,4]

comb_sor = ttk.Combobox(frame,value= list_text)
comb_sor.place(x=20,y=350,height =40, width=100)
comb_sor.set("english")

button_change = Button(frame,text="Translate", relief=RAISED)
button_change.place(x=140,y=350,height =40, width=100)


combo_dest= ttk.Combobox(frame,value=list_text)
combo_dest.place(x=300,y=350,height=40,width=100)
combo_dest.set("english")




root.mainloop()