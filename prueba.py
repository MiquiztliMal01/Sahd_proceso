from tkinter import*
import tkinter as tk
from tkinter import messagebox


root=Tk()
root.title('Usuario activo - Root')

frameAgregar=Frame(root)
frameAgregar.pack()
frameAgregar.config( width=450,height=300)
frameEliminar=Frame(root)
frameEliminar.pack()
frameModificar=Frame(root)
frameModificar.pack()

def limpiarCaja():
	e1nip.delete("1.0","end")

def salirAplicacion():
	valor=messagebox.askokcancel("Salir","¿Seguro que desea salir")
	if valor==True:
		root.destroy()
def agregarAplicacion():
	global frameAgregar
	frameEliminar.destroy()
	frameAgregar.destroy()
	frameModificar.destroy()
	frameAgregar=Frame(root)
	frameAgregar.pack()
	frameAgregar.config( width=450,height=300)
	titlabel=Label(frameAgregar,text="AGREGAR").place(x=215,y=20)
	niplabel=Label(frameAgregar,text="NIP:").place(x=50,y=50)
	nomlabel=Label(frameAgregar,text="NOMBRE(S):").place(x=50,y=90)
	ap_plabel=Label(frameAgregar,text="APELLIDO PATERNO:").place(x=50,y=130)
	ap_mlabel=Label(frameAgregar,text="APELLIDO MATERNO:").place(x=50,y=170)
	passlabel=Label(frameAgregar,text="CONTRASEÑA:").place(x=50,y=210)
	e1nip=tk.Entry(frameAgregar).place(x=175,y=50)
	e2nom=Entry(frameAgregar).place(x=175,y=90)
	e3app=Entry(frameAgregar).place(x=175,y=130)
	e4apm=Entry(frameAgregar).place(x=175,y=170)
	e5pass=Entry(frameAgregar).place(x=175,y=210)
	btregistrar=Button(frameAgregar,text="Registrar").place(x=350,y=70)
	btlimpiar=Button(frameAgregar,text="Limpiar",command=limpiarCaja).place(x=352,y=120)
	chuellas=Checkbutton(frameAgregar,text="Todas las huellas",onvalue=1, offvalue=0).place(x=320,y=170)
def eliminarAplicacion():
	global frameEliminar
	frameAgregar.destroy()
	frameEliminar.destroy()
	frameModificar.destroy()
	frameEliminar=Frame(root)
	frameEliminar.pack()
	frameEliminar.config(width=450,height=300)
	buslabel=Label(frameEliminar,text="Eliminar").place(x=215,y=10)
	opcionlabel=Label(frameEliminar,text="Seleccione la opción de eliminación, por favor:").place(x=30,y=50)
	Radiobutton(frameEliminar,text="NIP",value=1).place(x=130,y=70)
	Radiobutton(frameEliminar,text="Nombre completo",value=2).place(x=200,y=70)
	niplabel=Label(frameEliminar,text="NIP:").place(x=50,y=100)
	nomlabel=Label(frameEliminar,text="Nombre:").place(x=50,y=130)
	ap_plabel=Label(frameEliminar,text="Apellido paterno:").place(x=50,y=160)
	ap_mlabel=Label(frameEliminar,text="Apellido materno:").place(x=50,y=190)
	e1nip=Entry(frameEliminar).place(x=160,y=100)
	e2nom=Entry(frameEliminar).place(x=160,y=130)
	e3app=Entry(frameEliminar).place(x=160,y=160)
	e4apm=Entry(frameEliminar).place(x=160,y=190)
	btnelimiar=Button(frameEliminar,text="Eliminar").place(x=270,y=230)

def modificarAplicacion():
	global frameModificar
	frameAgregar.destroy()
	frameEliminar.destroy()
	frameModificar.destroy()
	frameModificar=Frame(root)
	frameModificar.pack()
	frameModificar.config(width=450,height=300)
	modlabel=Label(frameModificar,text="MODIFICAR").place(x=180,y=30)
	busniplabel=Label(frameModificar,text="BUSCAR POR NIP:").place(x=40,y=60)
	e1busnip=Entry(frameModificar).place(x=140,y=60)
	btbuscar=Button(frameModificar,text="Buscar").place(x=300,y=60)
barramenu=Menu(root)
root.config(menu=barramenu, width=450,height=300)

usumenu=Menu(barramenu,tearoff=0)
usumenu.add_command(label="Agregar",command=agregarAplicacion)
usumenu.add_command(label="Eliminar",command=eliminarAplicacion)
usumenu.add_command(label="Modificar",command=modificarAplicacion)
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