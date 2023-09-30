#Modules---------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
import random 

#Application ui--------------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.title("Word Guessing game")
root.geometry("300x210")

#Default List-----------------------------------------------------------------------------------------------------------------------------------------------
words = ["CPU","Laptop","Keyboard","Mouse","Moniter","Motherboard","Graphics Card","Storage"]
word = random.choice(words)

#Funtions-------------------------------------------------------------------------------------------------------------------------------------------------------
def done_funtion():
    b = user_entry.get()
    if b ==word:
        from tkinter import messagebox
        messagebox.showinfo("Correct","The gusses string is correct")
    else:
        from tkinter import messagebox
        messagebox.showerror("Wrong","The gussed string is wrong")

def next():
    global word
    word = random.choice(words)
    b = len(word)
    quiz_label_1.config(text=b,font=("word",18))
    user_entry.delete(0,END)

def hint_func():
    from tkinter import messagebox
    c = word[0]
    messagebox.showinfo("Hint",("The first letter is", c))

#Labels----------------------------------------------------------------------------------------------------------------------------------------------------------
quiz_label = Label(root,text="The number of letters is",font=("word",18))
quiz_label.place(x=0,y=60)

b = len(word)
quiz_label_1 = Label(root,text=b,font=("word",18))
quiz_label_1.place(x=239,y=60)

heading = Label(root,text="Guess The Text",font=("word",31))
heading.place(x=0,y=0)

user_entry_text = Label(root,text="Enter Guessed word",font=('word',18))
user_entry_text.place(x=40,y=100)

#Entry--------------------------------------------------------------------------------------------------------------------------------------------------------------
user_entry = Entry(root,width =38)
user_entry.place(x=40,y=130)

#Buttons--------------------------------------------------------------------------------------------------------------------------------------------------------------
done = Button(root,text="Check",font = ('word',18),command=done_funtion)
done.place(x=5,y=160)

refresh = Button(root,text="Next Word",font = ("word",18),command =next)
refresh.place(x=95,y=160)

hint = Button(root,text="Hint",font=("Word",18),command = hint_func)
hint.place(x=230,y=160)

#Mainloop-------------------------------------------------------------------------------------------------------------------------------------------------------------
root.mainloop()
#END