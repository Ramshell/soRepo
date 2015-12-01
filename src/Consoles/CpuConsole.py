from Tkinter import *
import codecs
import os


v0 = Tk()
v0.config(bg="black")
v0.geometry("700x500")
v1=Toplevel(v0)

def mostrar(ventana): ventana.deiconify()
def ocultar(ventana):ventana.withdraw()
def ejecutar(f): v0.after(200,f)

b1=Button(v0,text="CPU STATE",command=lambda: ejecutar(mostrar(v1)) or imprimir("hola") )
b1.grid(row=1,column=1)
b2=Button(v0,text="Hide CPU STATE",command=lambda: ejecutar(ocultar(v1)))
b2.grid(row=1,column=2)

def doit(f): v0.after(100, f)

def imprimir(textcontrol): print textcontrol.get('1.0', END+'-1c')

 

def escribir_en_archivo(enlace):

    f = codecs.open(enlace,"w","utf-8")

    texto = t1.get('1.0', END+'-1c')

    f.write(texto)

    f.close()

 

def abrir_archivo(enlace):

    if os.path.exists(enlace):

        f = open(enlace,"r")

        h= f.read()

        t1.insert(END,h)

        f.close()

 

t1=Text(v0)

t1.config(bg="black",fg="white")

t1.pack()

 

b3 = Button(v0,text="<< SAVE >>",command=lambda: doit(escribir_en_archivo('C:\hola.txt')))

b3.config(bg="black",fg="white")

b3.pack()

v1.withdraw()
v0.mainloop()
