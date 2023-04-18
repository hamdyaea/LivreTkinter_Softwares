import tkinter as tk

# Créer une fenêtre
window = tk.Tk()

# Créer une variable pour stocker l'option sélectionnée
selected_option = tk.StringVar()

# Créer un menu déroulant
option_menu = tk.OptionMenu(window, selected_option, "Option 1", "Option 2", "Option 3")

# Ajouter le menu déroulant à la fenêtre
option_menu.pack()

# Afficher la fenêtre
window.mainloop()
