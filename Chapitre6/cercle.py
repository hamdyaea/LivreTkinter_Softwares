import tkinter as tk

# Créer une fenêtre
window = tk.Tk()

# Créer un widget Canvas
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

# Dessiner un cercle
circle = canvas.create_oval(50, 50, 100, 100, fill="blue")

# Fonction pour mettre à jour le cercle
def update_circle():
    canvas.move(circle, 10, 0)
    window.after(50, update_circle)

# Mettre à jour le cercle
update_circle()

# Afficher la fenêtre
window.mainloop()
