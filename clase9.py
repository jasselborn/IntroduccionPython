import tkinter as tk
from tkinter import messagebox

tipos_dolar = {
    "Dólar BNA": 1515.00,
    "Dólar Blue": 1520.00,
    "Dólar MEP": 41561.04,
    "Dólar Mayorista": 1511.97,
    "Dólar CCL": 1580.85,
    "Dólar Turista": 1969.50
}

def convertir():
    try:
        cantidad = float(entry_cantidad.get())
        seleccion = lista_dolares.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un tipo de dólar de la lista.")
            return
        item = lista_dolares.get(seleccion)
        
        tipo = item.split(" - ")[0]
        valor = tipos_dolar[tipo]
        resultado = cantidad * valor
        messagebox.showinfo("Resultado", f"{cantidad} USD en {tipo} ({valor}) = {resultado} pesos")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido.")

ventana = tk.Tk()
ventana.title("Conversor de Dólares")
ventana.geometry("400x300")

tk.Label(ventana, text="Cantidad de dólares a convertir:").pack(pady=5)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack(pady=5)

tk.Label(ventana, text="Seleccione el tipo de dólar:")
lista_dolares = tk.Listbox(ventana, height=6, width=30)
for dolar, valor in tipos_dolar.items():
    lista_dolares.insert(tk.END, f"{dolar} - {valor}")
lista_dolares.pack(pady=5)

boton = tk.Button(ventana, text="Convertir", command=convertir)
boton.pack(pady=10)

ventana.mainloop()
