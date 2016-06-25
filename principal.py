from tkinter import *
from tkinter.messagebox import showinfo
#aprendiendo a usar p(Pythom-MySQL-Tkinter-Github)
#autor: Winston Junior Rodriguez Stand
#estudiante de ingenieria de sistemas

import MySQLdb
def iniciar():
    usuario = user.get()
    contrasena = contra.get()
    try:
        bd = MySQLdb.connect("localhost", "root", "", "login")
        try:
            cursor=bd.cursor()
            if (cursor.execute("SELECT * FROM `acceso` WHERE `usuario`='" + usuario +"'AND `contra`='" + contrasena + "'")):
                bd.commit()
                showinfo("Mensaje", "Inicio con exito")
                bd.close()
            else:
                bd.commit()
                showinfo("Mensaje", "Usuario no existe, por favor registrese")

        except:
            showinfo("Mensaje", "Usuario no existe, por favor registrese")
    except MySQLdb.OperationalError:
        showinfo("Mensaje", "No se pudo conectar a la base de datos, Pongase en contacto con el desarrollador")


def registrar():
    registrarventana = Toplevel()
    registrarventana.title("Registrar")
    registrarventana.geometry("600x600")
    registrarventana.config(bg="#6E6E6E")
    #imagenregis = PhotoImage(file="registrar.png")
    #etiquetaRegi = Label(registrarventana, image=imagenregis).place(x=50, y=30)
    nombre = Label(registrarventana, text="Nombres", bg="#6E6E6E", fg="#000000", font="Arial").place(x=150, y=100)
    nom = StringVar()
    cajaNom = Entry(registrarventana, textvariable=nom).place(x=250, y=100)
    apellido = Label(registrarventana, text="Apellidos", bg="#6E6E6E", fg="#000000", font="Arial").place(x=150, y=150)
    apel = StringVar()
    cajaApe = Entry(registrarventana, textvariable=apel).place(x=250, y=150)
    fecha = Label(registrarventana, text="Fecha de Nacimiento", bg="#6E6E6E", fg="#000000", font="Arial").place(x=100, y=200)
    fec = StringVar()
    cajaFe = Entry(registrarventana, textvariable=fec).place(x=270, y=200)
    email = Label(registrarventana, text="Email", bg="#6E6E6E", fg="#000000", font="Arial").place(x=150, y=250)
    ema = StringVar()
    cajaEmail = Entry(registrarventana, textvariable=ema).place(x=250, y=250)
    contra = Label(registrarventana, text="Contraseña", bg="#6E6E6E", fg="#000000", font="Arial").place(x=150, y=300)
    con = StringVar()
    cajaContra = Entry(registrarventana, textvariable=con).place(x=250, y=300)
    def registrarUs():
        emaUs = ema.get()
        contraUs = con.get()
        value = (emaUs, contraUs)
        try:
            db = MySQLdb.connect("localhost", "root", "", "login")
            showinfo("mensaje", "Exito")
            try:
                cursor = db.cursor()
                sql = "INSERT INTO acceso (usuario, contra) VALUES (%s, %s)"
                cursor.execute(sql, value)
                db.commit()
                showinfo("Exito", "Agregado con exito")
                db.close()
                ema.set("")
                con.set("")
            except:
                showinfo("Error", "Ocurrio un error")
                db.rollback()
        except MySQLdb.OperationalError:
            showinfo("No se pudo conectar")
    Registrar = Button(registrarventana, text="Registrar", bg="#01DF01", fg="#000000", font="Arial", command=registrarUs).place(x=300, y=350)




root = Tk()
root.geometry("600x600")
root.config(bg="#6E6E6E")
Usuario = Label(root, text="Usuario/Email", bg="#6E6E6E", fg="#000000", font="Arial").place(x=150, y =260)
user = StringVar()
cajaUser = Entry(root, textvariable=user).place(x=300, y=260)
password = Label(root, text="Contraseña", bg="#6E6E6E", fg="#000000", font="Arial").place(x=150, y = 320)
contra = StringVar()
cajaPass = Entry(root, show="*", textvariable=contra).place(x=300, y =320)
iniciar = Button(root, text="Iniciar Sesion", bg="#01DF01", fg="#000000", font="Arial", command=iniciar).place(x=250, y=400)
registrar = Button(root, text="Registrar", bg="#DF0101", fg="#000000", font="Arial", command=registrar).place(x=370, y =400)
root.mainloop()
