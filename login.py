from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as tk

pantalla=Tk()
pantalla.title("Bienvenido")
pantalla.geometry("450x300")

log=Label(pantalla,text="Login")
log.pack(anchor=CENTER)
log.config(font=("Arial",40))


usu=Label(pantalla, text="Usuario")
usu.place(x=70,y=100)
usu.config(font=("Arial",20))
pasw=Label(pantalla, text="Contraseña")
pasw.place(x=70,y=170)
pasw.config(font=("Arial",20))

e1=Entry(pantalla, bd=5)
e1.place(x=230,y=100)
e2=Entry(pantalla,bd=5,show="*")
e2.place(x=230,y=170)

def VentanaMenu():
	new=tk.Toplevel(root)

def login():
 db=sqlite3.connect("BDSAHD.db")
 c=db.cursor()

 usuario=e1.get()
 password=e2.get()

 c.execute('SELECT * FROM general WHERE id_usu = ? AND pass=?',(usuario, password) )
 
 if c.fetchall():
    messagebox.showinfo(title="Login correcto", message="Ingresar")
    c.execute('SELECT * FROM general WHERE id_cargo=Root')
    messagebox.showinfo(title="Root", message="Entro root")
 else:
   messagebox.showerror(title="Incorrecto", message="Datos erroneos")
   e1.delete(0, END)
   e1.insert(0, "")
   e2.delete(0,END)
   e2.insert(0,"")
 c.close()

bingresar=Button(pantalla,text="Ingresar", command=login)
bingresar.config(font=("Arial",20))
bingresar.place(x=165,y=225)

pantalla.mainloop()