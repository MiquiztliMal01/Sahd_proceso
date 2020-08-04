import pymysql
from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as tk
from tkinter import ttk

root=Tk()
root.title('Principal...')

frameAgregar=Frame(root)
root.withdraw()
frameAgregar.pack()
frameAgregar.config( width=450,height=300)
frameEliminar=Frame(root)
frameEliminar.pack()
frameModificar=Frame(root)
frameModificar.pack()
frameVisualizar=Frame(root)
frameVisualizar.pack()
frameFalyJus=Frame(root)
frameFalyJus.pack()

def agregarAplicacion():
    global frameAgregar
    frameAgregar.destroy()
    frameEliminar.destroy()
    frameModificar.destroy()
    frameVisualizar.destroy()
    frameAgregar=Frame(root)
    frameAgregar.pack()
    frameAgregar.config( width=450,height=300)
    titlabel=Label(frameAgregar,text="AGREGAR").place(x=215,y=20)
    niplabel=Label(frameAgregar,text="NIP:").place(x=50,y=50)
    nomlabel=Label(frameAgregar,text="NOMBRE(S):").place(x=50,y=90)
    ap_plabel=Label(frameAgregar,text="APELLIDO PATERNO:").place(x=50,y=130)
    ap_mlabel=Label(frameAgregar,text="APELLIDO MATERNO:").place(x=50,y=170)
    passlabel=Label(frameAgregar,text="CONTRASEÑA:").place(x=50,y=210)
    cargolabel=Label(frameAgregar,text="CARGO:").place(x=50,y=250)
    e1nip=Entry(frameAgregar).place(x=175,y=50)
    e2nom=Entry(frameAgregar).place(x=175,y=90)
    e3app=Entry(frameAgregar).place(x=175,y=130)
    e4apm=Entry(frameAgregar).place(x=175,y=170)
    e5pass=Entry(frameAgregar).place(x=175,y=210)
    btregistrar=Button(frameAgregar,text="Registrar").place(x=350,y=70)
    btlimpiar=Button(frameAgregar,text="Limpiar").place(x=352,y=120)
    chuellas=Checkbutton(frameAgregar,text="Todas las huellas",onvalue=1, offvalue=0).place(x=320,y=170)
    ccargo=tk.StringVar()
    cargoss=('Usuario','Administrador','Root')
    cmbcargo=ttk.Combobox(frameAgregar,width=20,textvariable=ccargo,values=cargoss,state="reandoly").place(x=175,y=250)

def eliminarAplicacion():
    global frameEliminar
    frameAgregar.destroy()
    frameEliminar.destroy()
    frameModificar.destroy()
    frameVisualizar.destroy()
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
    frameVisualizar.destroy()
    frameModificar=Frame(root)
    frameModificar.pack()
    frameModificar.config(width=450,height=300)
    modlabel=Label(frameModificar,text="MODIFICAR").place(x=180,y=30)
    busniplabel=Label(frameModificar,text="BUSCAR POR NIP:").place(x=40,y=60)
    e1busnip=Entry(frameModificar).place(x=140,y=60)
    btbuscar=Button(frameModificar,text="Buscar").place(x=300,y=60)
    bteditar=Button(frameModificar,text="Editar").place(x=370,y=60)
    lblnom=Label(frameModificar,text="NOMBRE(S):").place(x=50,y=100)
    lblap=Label(frameModificar,text="APELLIDO PATERNO:").place(x=50,y=130)
    lblam=Label(frameModificar,text="APELLIDO MATERNO:").place(x=50,y=160)
    lblpass=Label(frameModificar,text="CONTRASEÑA:").place(x=50,y=190)
    lblcargo=Label(frameModificar,text="CARGO:").place(x=50,y=220)
    txtnom=Entry(frameModificar).place(x=180,y=100)
    txtap=Entry(frameModificar).place(x=180,y=130)
    txtam=Entry(frameModificar).place(x=180,y=160)
    txtpass=Entry(frameModificar).place(x=180,y=190)
    ccargo=tk.StringVar()
    cargoss=('Usuario','Administrador')
    cmbcargo=ttk.Combobox(frameModificar,width=20,textvariable=ccargo,values=cargoss,state="reandoly").place(x=180,y=220)
    btnguardar=Button(frameModificar,text="GUARDAR").place(x=350,y=150)

def visualizarAplicacion():
    global frameVisualizar
    frameAgregar.destroy()
    frameEliminar.destroy()
    frameModificar.destroy()
    frameVisualizar.destroy()
    frameVisualizar=Frame(root)
    frameVisualizar.pack()
    frameVisualizar.config(width=450,height=300)
    lblencabezado=Label(frameVisualizar,text="Usuarios:").place(x=180,y=10)
    #mostrar datos por medio de una tabla /https://riptutorial.com/es/tkinter/example/31880/treeview--ejemplo-basico
def salirAplicacion():
    valor=messagebox.askokcancel("Salir","¿Seguro que desea salir")
    if valor==True:
        root.destroy()

def falyjusAplicacion():
    global frameFalyJus
    frameAgregar.destroy()
    frameEliminar.destroy()
    frameModificar.destroy()
    frameVisualizar.destroy()
    frameFalyJus.destroy()
    frameFalyJus=Frame(root)
    frameFalyJus.pack()
    frameFalyJus.config(width=450,height=300)
    lblencabezado=Label(frameFalyJus,text="FALTAS Y JUSTIFICANTES").place(x=180,y=10)
    lblnip=Label(frameFalyJus,text="NIP:").place(x=50,y=30)

def ventanaRoot():
    global root
    root=Tk()
    root.title('Ingreso como Root')
    barramenu=Menu(root)
    root.config(menu=barramenu, width=450,height=300)
    usumenu=Menu(barramenu,tearoff=0)
    usumenu.add_command(label="Agregar",command=agregarAplicacion)
    usumenu.add_command(label="Eliminar",command=eliminarAplicacion)
    usumenu.add_command(label="Modificar",command=modificarAplicacion)
    usumenu.add_separator()
    usumenu.add_command(label="Visualizar",command=visualizarAplicacion)
    usumenu.add_command(label="Salir",command=salirAplicacion)

    repmenu=Menu(barramenu,tearoff=0)
    repmenu.add_command(label="Faltas y justificaciones",command=falyjusAplicacion)
    repmenu.add_command(label="Pagos")

    ayumenu=Menu(barramenu,tearoff=0)
    ayumenu.add_command(label="Acerca de...")
    ayumenu.add_separator()
    ayumenu.add_command(label="Cerrar sesión")

    barramenu.add_cascade(label="Usuarios",menu=usumenu)
    barramenu.add_cascade(label="Reportes",menu=repmenu)
    barramenu.add_cascade(label="Ayuda",menu=ayumenu)

    root.mainloop()

def ventanaAdmon():
    admon=Tk()
    admon.title('Ingreso como Administrador')

def validar():
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
                    pantalla.withdraw()
                    if usu=='00001' or usu=='1':
                        print('root')
                        ventanaRoot()
                    if usu=='00002' or usu=='2':
                        print('admon')
                        ventanaAdmon()
                    else:
                        messagebox.showwarning(title="Acceso denegado",message="No posee los permisos necesarios para acceder a los datos.")
                else:
                    messagebox.showerror(title="Incorrecto",message="Datos erroneos")
                    e1.delete(0,END)
                    e1.insert(0,"")
                    e2.delete(0,END)
                    e2.insert(0,"")
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrio un error al conectar: ", e)

#def Registrar():
    

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

bingresar=Button(pantalla,text="Ingresar", command=validar)
bingresar.config(font=("Arial",20))
bingresar.place(x=165,y=225)

pantalla.mainloop()