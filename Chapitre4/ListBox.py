import tkinter as tk

# Créer une fenêtre
window = tk.Tk()

# Créer une Listbox
listbox = tk.Listbox(window)

# Ajouter des éléments à la Listbox
for i in range(50):
    listbox.insert(tk.END, "Element " + str(i+1))

# Créer une barre de défilement verticale
scrollbar_y = tk.Scrollbar(window, orient=tk.VERTICAL)

# Associer la barre de défilement à la Listbox
listbox.config(yscrollcommand=scrollbar_y.set)
scrollbar_y.config(command=listbox.yview)

# Placer la Listbox et la barre de défilement dans la fenêtre
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

# Afficher la fenêtre
window.mainloop()
