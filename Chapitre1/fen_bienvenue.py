import tkinter as tk

# Créer la fenêtre principale
window = tk.Tk()

# Titre de la fenêtre
window.title("Ma première fenêtre Tkinter")

# Ajouter une étiquette
label = tk.Label(window, text="Bienvenue sur mon premier programme Tkinter!")
label.pack()

# Afficher la fenêtre
window.mainloop()
