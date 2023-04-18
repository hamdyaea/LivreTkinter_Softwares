import tkinter as tk

# Créer une fonction pour gérer le clic sur le bouton
def on_button_click():
    print("Bouton cliqué !")

# Créer une fenêtre Tkinter
window = tk.Tk()

# Créer un bouton Tkinter
button = tk.Button(window, text="Cliquez ici", command=on_button_click)
button.pack()

# Afficher la fenêtre Tkinter
window.mainloop()
