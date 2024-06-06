import tkinter as tk
import json
from tkinter import messagebox

color_fondo = "#ffa8ff"
color_texto = "#66a3ff"
color_salir = "#f50505"

InformeDeCompras = tk.Tk()
InformeDeCompras.title("Informe")
InformeDeCompras.configure(bg=color_fondo)
InformeDeCompras.geometry("850x850")

lista = tk.Listbox(InformeDeCompras, width=90, height=125)
lista.pack(pady=90)

InformeDeCompras.mainloop()