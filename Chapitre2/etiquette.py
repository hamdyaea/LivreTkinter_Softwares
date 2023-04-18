import tkinter as tk

# Créer la fenêtre principale
window = tk.Tk()

# Créer une étiquette
label = tk.Label(window, text="Bonjour Tkinter!")

# Ajouter l'étiquette à la fenêtre
label.pack()

# Afficher la fenêtre
window.mainloop()
