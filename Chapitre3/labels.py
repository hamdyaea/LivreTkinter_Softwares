import tkinter as tk

# Créer une fenêtre
window = tk.Tk()

# Créer trois étiquettes
label1 = tk.Label(window, text="Label 1")
label2 = tk.Label(window, text="Label 2")
label3 = tk.Label(window, text="Label 3")

# Placer les étiquettes dans la fenêtre
label1.pack()
label2.pack()
label3.pack()

# Afficher la fenêtre
window.mainloop()
