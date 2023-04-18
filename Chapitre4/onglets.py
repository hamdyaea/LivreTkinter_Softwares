import tkinter as tk
from tkinter import ttk

# Créer une fenêtre
window = tk.Tk()

# Créer un widget Notebook
notebook = ttk.Notebook(window)

# Créer le premier onglet et y placer une étiquette
tab1 = ttk.Frame(notebook)
label1 = tk.Label(tab1, text="Hello from tab 1!")
label1.pack()
notebook.add(tab1, text="Tab 1")

# Créer le deuxième onglet et y placer une étiquette
tab2 = ttk.Frame(notebook)
label2 = tk.Label(tab2, text="Greetings from tab 2!")
label2.pack()
notebook.add(tab2, text="Tab 2")

# Placer le widget Notebook dans la fenêtre
notebook.pack()

# Afficher la fenêtre
window.mainloop()
