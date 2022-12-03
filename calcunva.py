from tkinter import *
from math import *
root=Tk()
root.title("Calculadora científica")
root.geometry("400x630")
root.resizable(0,0)
root.configure(bg="gray42")

color_boton= "grey99"
ancho_boton=9
alto_boton=3

operador=""
texto_pantalla=StringVar()

def clear():
    global operador
    operador=""
    texto_pantalla.set("0")

def toca_boton(b):
    global operador
    operador+= str(b)
    texto_pantalla.set(operador)

def resultado():
    global operador
    try:
        r=str(eval(operador))
    except:
        r= "Error"
    texto_pantalla.set(r)

def borrar():
    pantalla.delete(0, END)
def borrar_uno():
    largo = len(pantalla.get())
    pantalla.delete(largo-1, END)

clear()

boton_uno=Button(root, text="1",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton(1)).grid(row=1,column=0, pady=10)

boton_dos=Button(root, text="2",bg=color_boton, width=ancho_boton, height= alto_boton,command=lambda: toca_boton(2)).grid(row=1,column=1, pady=10)

boton_tres=Button(root, text="3",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton(3)).grid(row=1,column=2, pady=10)

boton_cuatro=Button(root, text="4",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton(4)).grid(row=2,column=0, pady=10)

boton_cinco=Button(root, text="5",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton(5)).grid(row=2,column=1, pady=10)

boton_seis=Button(root, text="6",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton(6)).grid(row=2,column=2, pady=10)

boton_siete=Button(root, text="7",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton(7)).grid(row=3,column=0, pady=10)

boton_ocho=Button(root, text="8",bg=color_boton, width=ancho_boton, height= alto_boton,command=lambda: toca_boton(8)).grid(row=3,column=1, pady=10)

boton_nueve=Button(root, text="9",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton(9)).grid(row=3,column=2, pady=10)

boton_cero=Button(root, text="0",bg=color_boton, width=ancho_boton, height= alto_boton,command=lambda: toca_boton(0)).grid(row=4,column=0, pady=10)

boton_punto=Button(root, text=".",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton(".")).grid(row=4,column=1, pady=10)

oton_porcentaje=Button(root, text="%",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton("%")).grid(row=4,column=2, pady=10)

boton_suma=Button(root, text="+",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton("+")).grid(row=1,column=3, pady=10)

boton_resta=Button(root, text="-",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton("-")).grid(row=2,column=3, pady=10)

boton_multiplicacion=Button(root, text="x",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton("*")).grid(row=3,column=3, pady=10)

boton_division=Button(root, text="/",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton("/")).grid(row=4,column=3, pady=10)

boton_pi=Button(root, text="π",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton("pi")).grid(row=5,column=0, pady=10)

boton_raiz=Button(root, text="√",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton("sqrt")).grid(row=5,column=1, pady=10)

boton_expo=Button(root, text="Ex",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton("exp")).grid(row=5,column=2, pady=10)

boton_clear_uno=Button(root, text="C",bg="red", width=ancho_boton, height= alto_boton, command= borrar_uno).grid(row=5,column=3, pady=10)

boton_clear=Button(root, text="AC",bg="red", width=ancho_boton, height= alto_boton, command= borrar).grid(row=6,column=3, pady=10)

boton_igual=Button(root, text="=",bg="red", width=ancho_boton, height= alto_boton, command=resultado).grid(row=7,column=3, pady=10)

boton_parentizq=Button(root, text="(",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton("(")).grid(row=6,column=0, pady=10)

boton_parentder=Button(root, text=")",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton(")")).grid(row=6,column=1, pady=10)

boton_rad=Button(root, text="RAD",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton("tan(radians")).grid(row=6,column=2, pady=10)

boton_sin=Button(root, text="sin",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton("sin(radians")).grid(row=7,column=0, pady=10)

boton_cos=Button(root, text="cos",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton("cos(radians")).grid(row=7,column=1, pady=10)

boton_tan=Button(root, text="tan",bg=color_boton, width=ancho_boton, height= alto_boton, command=lambda: toca_boton("tan")).grid(row=7,column=2, pady=10)


pantalla = Entry(root, font=("arial", 20, "bold"), width=22, borderwidth=10,bg="white", textvariable=texto_pantalla)

pantalla.grid(row=0, column=0, columnspan=4,padx=20,pady=20)

root.mainloop()