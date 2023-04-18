import tkinter as tk

# Créer une fenêtre
window = tk.Tk()

# Créer trois étiquettes
label1 = tk.Label(window, text="Label 1")
label2 = tk.Label(window, text="Label 2")
label3 = tk.Label(window, text="Label 3")

# Placer les étiquettes dans la fenêtre avec grid()
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)

# Afficher la fenêtre
window.mainloop()
