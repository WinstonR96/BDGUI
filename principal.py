#Elaborado por Winston Junior Rodriguez Stand - Estudiante 5to semestre de Ingenìeria de Sistemas
#importamos los modulos necesarios, en el caso "Tkinter (GUI) y MySQLdb(Base de datos)"
from tkinter import *
from tkinter.messagebox import showinfo
import MySQLdb

#definimos metodos que seran utilizados
def iniciar():
    #Validamos campos vacios
    if(user.get()=="" or contra.get()==""):
        showinfo("Error", "Rellene campos vacios")
    else:
        #extraemos los datos de las cajas de texto
        usuario = user.get()
        passw = contra.get()

        try:#inteentamos conectar a la base de datos
            bd = MySQLdb.connect("localhost", "root", "", "setup")
            try:
                cursor = bd.cursor()
                if(cursor.execute("SELECT * FROM `login` WHERE `usuario`='" + usuario +"'AND `contra`='" + passw + "'")):
                    bd.commit()
                    bd.close()
                    #root.destroy()
                    principal()

                else:
                    bd.commit()
                    showinfo("Invalido", "Email/Contraseña invalida")
            except:
                showinfo("Error", "Ha ocurrido un error")
        except MySQLdb.OperationalError:
            showinfo("Error", "No se pudo conectar a la base de datos, pongase en contacto con el desarrollador")

def principal():
    principal = Toplevel()
    principal.title("Principal")
    principal.geometry("600x600")



def Ventanaregistrar():
    registrarventana = Toplevel()
    registrarventana.title("Registrar")
    registrarventana.geometry("600x600")
    registrarventana.config(bg="#6E6E6E")
    # imagenregis = PhotoImage(file="registrar.png")
    # etiquetaRegi = Label(registrarventana, image=imagenregis).place(x=50, y=30)
    nombre = Label(registrarventana, text="Nombres", bg="#6E6E6E", fg="#000000", font="Arial").place(x=150, y=100)
    nom = StringVar()
    cajaNom = Entry(registrarventana, textvariable=nom).place(x=250, y=100)
    apellido = Label(registrarventana, text="Apellidos", bg="#6E6E6E", fg="#000000", font="Arial").place(x=150, y=150)
    apel = StringVar()
    cajaApe = Entry(registrarventana, textvariable=apel).place(x=250, y=150)
    sexo = Label(registrarventana, text="Sexo", bg="#6E6E6E", fg="#000000", font="Arial").place(x=150,y=200)
    sex = StringVar()
    cajaSex = Entry(registrarventana, textvariable=sex).place(x=250, y=200)
    email = Label(registrarventana, text="Email", bg="#6E6E6E", fg="#000000", font="Arial").place(x=150, y=250)
    ema = StringVar()
    cajaEmail = Entry(registrarventana, textvariable=ema).place(x=250, y=250)
    contra = Label(registrarventana, text="Contrasena", bg="#6E6E6E", fg="#000000", font="Arial").place(x=150, y=300)
    con = StringVar()
    cajaContra = Entry(registrarventana, textvariable=con, show="*").place(x=250, y=300)
    recontra = Label(registrarventana, text="Repetir", bg="#6E6E6E", fg="#000000", font="Arial").place(x=150, y=350)
    recon = StringVar()
    cajaReContra = Entry(registrarventana, textvariable=recon, show="*").place(x=250, y=350)
    def registrarUs():
        if(nom.get()=="" or apel.get()=="" or sex.get()=="" or ema.get()=="" or con.get()==""):
            showinfo("Falta Informacion", "Rellene informacion faltante")
        elif (con.get() != recon.get()):
            showinfo("Invalida", "Contrasena no coincide")
        else:
            nombres= nom.get()
            apellidos = apel.get()
            genero = sex.get()
            usuario = ema.get()
            contra = con.get()
            value = (nombres, apellidos,genero,usuario,contra)
            try:
                bd = MySQLdb.connect("localhost", "root", "", "setup")
                try:
                    cursor = bd.cursor()
                    sql = "INSERT INTO login (nombres, apellidos, sexo, usuario, contra) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql, value)
                    bd.commit()
                    showinfo("Exito", "Registrado con exito, ya puede acceder al sistema")
                    bd.close()
                    nom.set("")
                    apel.set("")
                    sex.set("")
                    ema.set("")
                    con.set("")
                    recon.set("")

                except:
                    bd.rollback()
                    showinfo("Error", "Ocurrio un error")

            except MySQLdb.OperationalError:
                showinfo("Error", "No se puedo conectar a la base de datos, pongase en contacto con el desarrollador")


    def salir():
        registrarventana.destroy()
    Registrar = Button(registrarventana, text="Registrar", bg="#01DF01", fg="#000000", font="Arial", command=registrarUs).place(x=300, y=500)
    volver = Button(registrarventana, text="volver", bg="#DF0101", fg="#000000", font="Arial",command=salir).place(x=400, y=500)


#creamos la ventana principal que sera para loguearse
root = Tk()
root.geometry("600x600")#dimension de la ventana
root.config(bg="#6E6E6E")
Usuario = Label(root, text="Usuario/Email", bg="#6E6E6E", fg="#000000", font="Arial").place(x=150, y =260)
user = StringVar()
cajaUser = Entry(root, textvariable=user).place(x=300, y=260)
password = Label(root, text="Password", bg="#6E6E6E", fg="#000000", font="Arial").place(x=150, y = 320)
contra = StringVar()
cajaPass = Entry(root, show="*", textvariable=contra).place(x=300, y =320)
iniciar = Button(root, text="Iniciar Sesion", bg="#01DF01", fg="#000000", font="Arial", command=iniciar).place(x=250, y=400)
registrar = Button(root, text="Registrar", bg="#DF0101", fg="#000000", font="Arial", command=Ventanaregistrar).place(x=370, y =400)
root.mainloop()