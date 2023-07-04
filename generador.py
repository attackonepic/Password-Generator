import random
import string
import tkinter as tk
window = tk.Tk()

symbols = "!@#$%^&*()_-.:,;=[]{}"
simbolos = random.choices(symbols, k=4)
mayusculas = random.choices(string.ascii_uppercase, k=6)   
minusculas = random.choices(string.ascii_lowercase, k=6)
numeros = [random.randint(1, 10) for _ in range(4)]
password = ""
salasana = ""
for item in simbolos:
    password += item
for mayuscula in mayusculas:
    password += mayuscula
for minuscula in minusculas:
    password += minuscula
for numero in numeros:
    password += str(numero)

def uusi_salasana():
    global salasana
    salasana = ""

    passi = random.choices(password, k=10)
    for passit in passi:
        salasana += passit
    valor["text"] = salasana


def copy_string():
    global salasana
    string_to_copy = salasana

    window.clipboard_clear()
    window.clipboard_append(string_to_copy)


window.rowconfigure(2, minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)

roll = tk.Button(master=window, text="New Password", command=uusi_salasana)
copiar = tk.Button(master=window, text="Copy", command=copy_string)

roll.grid(row=0, column=0, sticky="nsew")
valor = tk.Label(master=window, text=" ")
valor.grid(row=1, column=0, sticky="nsew")
copiar.grid(row=2, column=0, sticky="nsew")


window.grid_rowconfigure(0, minsize=50)
window.grid_rowconfigure(1, minsize=50)

window.title("Password Generator")
window.mainloop()


