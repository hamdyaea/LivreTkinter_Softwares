import tkinter as tk
import random

# Créer une fenêtre
window = tk.Tk()

# Créer un widget Canvas
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

# Créer un cercle
circle = canvas.create_oval(50, 50, 100, 100, fill="blue")

# Fonction pour mettre à jour les cercles
def update_circles():
    # Déplacer le cercle
    x1, y1, x2, y2 = canvas.coords(circle)
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    canvas.move(circle, dx, dy)
    
    # Appeler la fonction de manière répétée
    window.after(50, update_circles)

# Appeler la fonction de manière initiale
update_circles()

# Lancer la boucle principale de l'application
window.mainloop()
