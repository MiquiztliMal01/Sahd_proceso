import pymysql
from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as ttk

def _init_ (self):
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

def principal():
	print('Principal en ejecución')
	pantalla.destroy()

def limpiarCaja():
	e1nip.delete("1.0","end")

def login():
	usu=e1.get()
	passc=e2.get()
	try:
		conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='bdsahd')
		try:
			with conexion.cursor() as cursor:
				sql="SELECT * FROM usuarios WHERE id_usu=%s AND contra=%s"
				cursor.execute(sql,(usu,passc))
				if cursor.fetchall():
					pantalla.destroy()
					if usu=='00001' or usu=='1':
						
						root=Tk()
						root.title('Usuario activo - Root')

						def salirAplicacion():
							valor=messagebox.askokcancel("Salir","¿Seguro que desea salir")
							if valor==True:
								root.destroy()

						print("Root")
						barramenu=Menu(root)
						root.config(menu=barramenu, width=450,height=300)

						usumenu=Menu(barramenu,tearoff=0)
						usumenu.add_command(label="Agregar")
						usumenu.add_command(label="Eliminar")
						usumenu.add_command(label="Modificar")
						usumenu.add_separator()
						usumenu.add_command(label="Visualizar")
						usumenu.add_command(label="Salir",command=salirAplicacion)

						repmenu=Menu(barramenu,tearoff=0)
						repmenu.add_command(label="Faltas y justificaciones")
						repmenu.add_command(label="Pagos")

						ayumenu=Menu(barramenu,tearoff=0)
						ayumenu.add_command(label="Acerca de...")
						ayumenu.add_separator()
						ayumenu.add_command(label="Cerrar sesión")

						barramenu.add_cascade(label="Usuarios",menu=usumenu)
						barramenu.add_cascade(label="Reportes",menu=repmenu)
						barramenu.add_cascade(label="Ayuda",menu=ayumenu)



						root.mainloop()
					else:
						print("Otro")

				else:
					messagebox.showerror(title="Incorrecto", message="Datos erroneos")
					e1.delete(0, END)
					e1.insert(0, "")
					e2.delete(0,END)
					e2.insert(0,"")
		finally:
			conexion.close()
		
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)

bingresar=Button(pantalla,text="Ingresar", command=login)
bingresar.config(font=("Arial",20))
bingresar.place(x=165,y=225)

pantalla.mainloop()
