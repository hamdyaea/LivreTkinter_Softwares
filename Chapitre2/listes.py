import tkinter as tk

# Créer la fenêtre principale
window = tk.Tk()

# Créer une liste
listbox = tk.Listbox(window)

# Ajouter des éléments à la liste
listbox.insert(1, "Option 1")
listbox.insert(2, "Option 2")
listbox.insert(3, "Option 3")

# Ajouter la liste à la fenêtre
listbox.pack()

# Afficher la fenêtre
window.mainloop()
