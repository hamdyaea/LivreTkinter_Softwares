import tkinter as tk

# Créer une fenêtre
window = tk.Tk()

# Créer une étiquette
label = tk.Label(window, text="Hello, world!")

# Placer l'étiquette dans la fenêtre avec place()
# x est l’horizontal et y le vertical
label.place(x=50, y=50)

# Afficher la fenêtre
window.mainloop()
