import pymysql
from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as ttk

root=Tk()
root.title('Principal...')

frameAgregar=Frame(root)
root.withdraw()
frameAgregar.pack()
frameAgregar.config( width=450,height=300)

def agregarAplicacion():
    global frameAgregar
    frameAgregar.destroy()
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

def ventanaRoot():
    global root
    root=Tk()
    root.title('Ingreso como Root')
    barramenu=Menu(root)
    root.config(menu=barramenu, width=450,height=300)
    usumenu=Menu(barramenu,tearoff=0)
    usumenu.add_command(label="Agregar",command=agregarAplicacion)
    usumenu.add_command(label="Eliminar")
    usumenu.add_command(label="Modificar")
    usumenu.add_separator()
    usumenu.add_command(label="Visualizar")
    usumenu.add_command(label="Salir")

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