from tkinter import *
from tkinter import ttk
from tkinter import messagebox as message
import consultas

class app:
	def __init__(self, windows):
		self.wind = windows
		self.wind.title("SAHD")

		# Consultas y conexión a la BD
		self.query = consultas.query()
		
		#Ventana ROOT
		self.wind.geometry('420x310')
		menubar = Menu(root)
		root.config(menu=menubar)

		usuariomenu = Menu(menubar, tearoff=0)
		usuariomenu.add_command(label="Registrar",command=self.insert)
		usuariomenu.add_command(label="Eliminar",command=self.delete)
		usuariomenu.add_command(label="Editar",command=self.update)

		repmenu = Menu(menubar, tearoff=0)
		repmenu.add_command(label="Faltas y justificaciones")
		repmenu.add_command(label="Pagos")

		ayumenu = Menu(menubar, tearoff=0)
		ayumenu.add_command(label="Acerca de...")

		menubar.add_cascade(label="Usuarios", menu=usuariomenu)
		menubar.add_cascade(label="Reportes", menu=repmenu)
		menubar.add_cascade(label="Ayuda", menu=ayumenu)

	def insert(self):
		frame = LabelFrame(self.wind, text="Registrar")
		frame.grid(row=0, column=0, columnspan=3,ipadx=50)
		Label(frame,text="Nip: ").grid(row=1, column=1)
		self.nip = Entry(frame)
		self.nip.grid(row=1, column=2, pady=5)

		Label(frame,text="Nombre(s): ").grid(row=2, column=1)
		self.nom = Entry(frame)
		self.nom.grid(row=2, column=2, pady=10)

		Label(frame,text="Apellido Paterno: ").grid(row=3, column=1)
		self.ap_p = Entry(frame)
		self.ap_p.grid(row=3, column=2, pady=10)

		Label(frame,text="Apellido Materno: ").grid(row=4, column=1)
		self.ap_m = Entry(frame)
		self.ap_m.grid(row=4, column=2, pady=10)

		Label(frame,text="Contraseña: ").grid(row=5, column=1)
		self.contra = Entry(frame)
		self.contra.grid(row=5, column=2, pady=10)

		Label(frame,text="Huella: ").grid(row=6, column=1)
		self.huella = Entry(frame)
		self.huella.grid(row=6, column=2, pady=10)

		Label(frame,text="Cargo: ").grid(row=7, column=1)
		self.id_cargo = Entry(frame)
		self.id_cargo.grid(row=7, column=2, pady=10)

		#Btn enviar
		ttk.Button(frame, text="Guardar", command=self.guardar).grid(row=8, columnspan=3, sticky=W + E)

	def guardar(self):
		nom = self.nom.get()
		ap_p = self.ap_p.get()
		ap_m= self.ap_m.get()
		contra = self.contra.get()
		huella = self.huella.get()
		id_cargo = self.id_cargo.get()
		nip = self.nip.get()
		if(nom !='' and ap_p !='' and ap_m != '' and contra !='' and huella !='' and id_cargo !='' and nip !=''):
			self.query.save(nom,ap_p,ap_m,contra,huella,id_cargo,nip)
			message.showinfo(message="Datos almacenados", title="Guardados")
			self.nom.delete(0,END)
			self.ap_p.delete(0,END)
			self.ap_m.delete(0,END)
			self.contra.delete(0,END)
			self.huella.delete(0,END)
			self.id_cargo.delete(0,END)
			self.nip.delete(0,END)
		else:
			message.showinfo(message="Ingrese los datos", title="Por favor")  	

	def update(self):
		self.tabla0 = ttk.Treeview(height=20, columns=('#1', '#2', '#3','#4','#5','#6'))
		self.tabla0.grid(row=7, column=0)
		self.tabla0.heading("#0",text="Nip",anchor='w')
		self.tabla0.heading("#1",text="Nombre(s)",anchor='w')
		self.tabla0.heading("#2",text="Apellido Paterno",anchor='w')
		self.tabla0.heading("#3",text="Apellido Materno",anchor='w')
		self.tabla0.heading("#4",text="Contraseña",anchor='w')
		self.tabla0.heading("#5",text="Huella",anchor='w')
		self.tabla0.heading("#6",text="Cargo",anchor='w')
		self.mostrar()
		ttk.Button(text="Actualizar", command=self.actualizar).grid(row=10, column = 0)		

	def actualizar(self):
		try:
			self.previous_nip = self.tabla0.item(self.tabla0.selection())['text']
			self.previous_nom = self.tabla0.item(self.tabla0.selection())['values'][0]
			self.previous_ap_p = self.tabla0.item(self.tabla0.selection())['values'][1]
			self.previous_ap_m = self.tabla0.item(self.tabla0.selection())['values'][2]
			self.previous_contra = self.tabla0.item(self.tabla0.selection())['values'][3]
			self.previous_huella = self.tabla0.item(self.tabla0.selection())['values'][4]
			self.previous_id_cargo = self.tabla0.item(self.tabla0.selection())['values'][5]

			nip_set = StringVar()
			nip_set.set(self.previous_nip)
			nom_set = StringVar()
			nom_set.set(self.previous_nom)
			ap_p_set = StringVar()
			ap_p_set.set(self.previous_ap_p)
			ap_m_set = StringVar()
			ap_m_set.set(self.previous_ap_m)
			contra_set = StringVar()
			contra_set.set(self.previous_contra)
			huella_set = StringVar()
			huella_set.set(self.previous_huella)
			id_cargo_set = StringVar()
			id_cargo_set.set(self.previous_id_cargo)

			self.edit_window = Toplevel()
			self.edit_window.title("Actualizar")
			frame = LabelFrame(self.edit_window, text='Actualizar')
			frame.grid(row=0, column=0, ipadx=20)
			Label(frame, text="Nip: ").grid(row=1, column=1)
			self.new_nip = Entry(frame, textvar=nip_set)
			self.new_nip.grid(row=1,column=2,ipadx=20)

			Label(frame, text='Nombre(s): ').grid(row=2, column=1)
			self.new_nom = Entry(frame, textvar=nom_set)
			self.new_nom.grid(row=2,column=2,ipadx=20)

			Label(frame, text="Apellido Paterno: ").grid(row=3, column=1)
			self.new_ap_p = Entry(frame, textvar=ap_p_set)
			self.new_ap_p.grid(row=3,column=2,ipadx=20)

			Label(frame, text="Apellido Materno: ").grid(row=4, column=1)
			self.new_ap_m = Entry(frame, textvar=ap_m_set)
			self.new_ap_m.grid(row=4,column=2,ipadx=20)

			Label(frame, text="Contraseña: ").grid(row=5, column=1)
			self.new_contra = Entry(frame, textvar=contra_set)
			self.new_contra.grid(row=5,column=2,ipadx=20)

			Label(frame, text="Huella: ").grid(row=6, column=1)
			self.new_huella = Entry(frame, textvar=huella_set)
			self.new_huella.grid(row=6,column=2,ipadx=20)

			Label(frame, text="Cargo: ").grid(row=7, column=1)
			self.new_id_cargo = Entry(frame, textvar=id_cargo_set)
			self.new_id_cargo.grid(row=7,column=2,ipadx=20)

			ttk.Button(frame, text="Guardar", command=self.edit).grid(row=8, columnspan=2, sticky=W + E)
		except IndexError:
			message.showinfo(message="Por favor selecciona un dato de la tabla", title="Error")

	def edit(self):
		self.nip=self.new_nip.get()
		self.nom = self.new_nom.get()
		self.ap_p = self.new_ap_p.get()
		self.ap_m = self.new_ap_m.get()
		self.contra = self.new_contra.get()
		self.huella = self.new_huella.get()
		self.id_cargo = self.new_id_cargo.get()
	
		if(self.nip !='' and self.nom !='' and self.ap_p != '' and self.ap_m != '' and self.contra != '' and self.huella != ''):
			self.query.update(self.nip,self.nom,self.ap_p,self.ap_m,self.contra,self.huella,self.id_cargo,
							  self.previous_nip,self.previous_nom,self.previous_ap_p,self.previous_ap_m,self.previous_contra,
							  self.previous_huella,self.previous_id_cargo)
			self.mostrar()
			self.edit_window.destroy()

	def delete(self):
		self.tabla0 = ttk.Treeview(height=20, columns=('#1', '#2', '#3','#4','#5','#6'))
		self.tabla0.grid(row=7, column=0)
		self.tabla0.heading("#0",text="Nip",anchor='w')
		self.tabla0.heading("#1",text="Nombre(s)",anchor='w')
		self.tabla0.heading("#2",text="Apellido Paterno",anchor='w')
		self.tabla0.heading("#3",text="Apellido Materno",anchor='w')
		self.tabla0.heading("#4",text="Contraseña",anchor='w')
		self.tabla0.heading("#5",text="Huella",anchor='w')
		self.tabla0.heading("#6",text="Cargo",anchor='w')
		self.mostrar()
		ttk.Button(text="Eliminar", command=self.eliminar).grid(row=10, column = 0)

	def mostrar(self):
		delete = self.tabla0.get_children()
		for elemento in delete:
			self.tabla0.delete(elemento)
		rows = self.query.read()
		for row in rows:
			self.tabla0.insert('',END, text=row[7],value=row[1:])

	def eliminar(self):
		try:
			nom = self.tabla0.item(self.tabla0.selection())['values'][0]
			self.query.delete(nom)
			self.mostrar()
		except IndexError:
			message.showinfo(message="Por favor selecciona un dato de la tabla", title="Error")


if __name__=="__main__":
	root = Tk()
	Aplicacion = app(root)
	root.mainloop()