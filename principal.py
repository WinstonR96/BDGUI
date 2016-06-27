#Elaborado por Winston Junior Rodriguez Stand - Estudiante 5to semestre de Ingenìeria de Sistemas
#importamos los modulos necesarios, en el caso "Tkinter (GUI) y MySQLdb(Base de datos)"
from tkinter import *
from tkinter.messagebox import showinfo
import MySQLdb

#definimos metodos que seran utilizados
def iniciar():#metodo para iniciar sesion
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


def principal():#metodo para definir la ventana, luego de iniciar sesion
    pri = Toplevel()
    pri.title("Principal")
    pri.geometry("600x600")
    pri.config(bg="#6E6E6E")
    def vencrear():
        c = Toplevel()
        c.title("Insertar nota")
        c.geometry("600x600")
        c.config(bg="#6E6E6E")
        titulo = Label(c, text="Titulo").place(x=100, y =100)
        til = StringVar()
        cajaTil = Entry(c,textvariable=til).place(x=250,y=100)
        cuerpo = Label(c, text="Cuerpo").place(x=100, y = 250)
        cu = StringVar()
        cajaCur = Entry(c, textvariable=cu, width=50).place(x=250, y=250)
        def insertar():
            if(til.get()=="" or cu.get()==""):
                showinfo("Error", "Rellene informacion")
            else:
                title = til.get()
                body = cu.get()
                val = (title, body)
                try:
                    bf = MySQLdb.connect("localhost", "root", "", "setup")
                    try:
                        query = bf.cursor()
                        sq = "INSERT INTO notas (titulo, cuerpo) VALUES (%s,%s)"
                        query.execute(sq, val)
                        bf.commit()
                        bf.close()
                        showinfo("Exito", "Agregada nota con exito")
                        til.set("")
                        cu.set("")
                    except:
                        bf.rollback()
                        showinfo("Error", "Ocurrio un error")
                except MySQLdb.OperationalError:
                    showinfo("Error", "No se puede conectar a la base de datos, pongase en contacto con el administrador")
        insertar = Button(c, text="Insertar", command=insertar).place(x=300, y=300)
    def venMostrar():
        m = Toplevel()
        m.title("Visualizar")
        m.geometry("600x600")
        m.config(bg="#6E6E6E")

        nomos = StringVar()
        #nota = Entry(m, textvariable=nomos).place(x=100, y=100)
        nota = Label(m, textvariable=nomos).place(x=100, y=100)
        def vis():
           try:
               nb = MySQLdb.connect("localhost", "root", "", "setup")
               try:
                   hp = nb.cursor()
                   qsl = "SELECT * FROM notas"
                   hp.execute(qsl)
                   resultado = hp.fetchall()
                   for registro in resultado:
                       titulo = registro[1]
                       cuerpo = registro[2]
                       #nomos.set("Titulo: "+titulo+"\nNota: "+cuerpo)
                       nomos.set("Titulo=%s, Cuerpo=%s" % (titulo, cuerpo))
                       print("Titulo=%s, Cuerpo=%s" % (titulo, cuerpo))
                       showinfo("Notas","Titulo=%s, Cuerpo=%s" % (titulo, cuerpo))

                   nb.close()
               except:
                   showinfo("Error", "Se ha producido un error")
           except MySQLdb.OperationalError:
                showinfo("Error", "No se puede conectar a la base de datos, pongase en contacto con el administrador")

        ver = Button(m, text="Ver", command=vis).place(x=400, y = 500)


    opcion = Label(pri, text="Elija una opcion", bg="#6E6E6E", fg="#000000", font="Arial").place(x=100, y=100)
    crear = Button(pri, text="Crear", command=vencrear).place(x=150, y=150)
    borrar = Button(pri, text="Eliminar").place(x=250, y=150)
    actualizar = Button(pri, text="Actualizar").place(x=150, y=250)
    mostrar = Button(pri, text="Ver", command=venMostrar).place(x=250, y =250)




def Ventanaregistrar():#metodo que abre el panel de registro
    registrarventana = Toplevel()
    registrarventana.title("Registrar")
    registrarventana.geometry("600x600")
    registrarventana.config(bg="#6E6E6E")
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
    def registrarUs(): #metodo para registrar
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