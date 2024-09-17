import tkinter as tk
from tkinter import messagebox

# Funciones para las operaciones matemáticas
def sumar():
    resultado = float(entrada1.get()) + float(entrada2.get())
    etiqueta_resultado.config(text=f"Resultado: {resultado}")

def restar():
    resultado = float(entrada1.get()) - float(entrada2.get())
    etiqueta_resultado.config(text=f"Resultado: {resultado}")

def multiplicar():
    resultado = float(entrada1.get()) * float(entrada2.get())
    etiqueta_resultado.config(text=f"Resultado: {resultado}")

def dividir():
    try:
        resultado = float(entrada1.get()) / float(entrada2.get())
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por cero")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear entradas de texto para los números
etiqueta1 = tk.Label(ventana, text="Número 1:")
etiqueta1.grid(row=0, column=0)

entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column=1)

etiqueta2 = tk.Label(ventana, text="Número 2:")
etiqueta2.grid(row=1, column=0)

entrada2 = tk.Entry(ventana)
entrada2.grid(row=1, column=1)

# Crear botones para las operaciones
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.grid(row=2, column=0)

boton_restar = tk.Button(ventana, text="Restar", command=restar)
boton_restar.grid(row=2, column=1)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multiplicar.grid(row=3, column=0)

boton_dividir = tk.Button(ventana, text="Dividir", command=dividir)
boton_dividir.grid(row=3, column=1)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado:")
etiqueta_resultado.grid(row=4, column=0, columnspan=2)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
