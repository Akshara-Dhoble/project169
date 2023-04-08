# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:12:52 2023

@author: Akshara Sagar Dhoble
"""

from tkinter import*
from tkinter import messagebox
from tkinter import ttk

root = Tk()

root.title("Classes")
root.geometry("500x500")

gui_elements = ["label" , "button" , "combo box " ]

dropdown = ttk.Combobox(root , state="readonly" , values=gui_elements)
dropdown.pack()

class createElements () :
    
    def __init__(self):
        print("Creating UI elements")    
    
    def clbl(self):
        lbl = Label(root , text = "Label")
        lbl.pack()
        
    def cbtn(self) :
        btn = Button(root , text="Button" , command=self.message)
        btn.pack(padx=20 , pady=10)
        
    def ccb(self) :
        val = [1,2,3,4,5]
        cb = ttk.Combobox(root , state="readonly" , values=val)
        cb.pack()
        
   
   
        
    def choose(self):
        global dropdown
        
        element = dropdown.get()
        
        if(element == "label"):
            self.clbl()
        
        elif(element == "button"):
            self.cbtn()
            
        elif(element == "combo box"):
            self.ccb()  
            
     
    
    def message(self):
        messagebox.showinfo("Message" , "You clicked the button using class .")
    
        
obj = createElements()



btn = Button(root , text="Create Elements", command = obj.choose)
btn.pack(padx=20 , pady=10)


root.mainloop()