import tkinter as tk

# Créer une fenêtre
window = tk.Tk()

# Créer un widget Canvas
canvas = tk.Canvas(window, width=500, height=500)

# Placer le widget Canvas dans la fenêtre
canvas.pack()

# Afficher la fenêtre
window.mainloop()
