import tkinter as tk

# Créer une fenêtre Tkinter
window = tk.Tk()

# Créer un canevas Tkinter
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

# Charger une image
photo = tk.PhotoImage(file="github.gif")

# Dessiner l'image
image = canvas.create_image(0, 0, image=photo, anchor=tk.NW)

# Afficher la fenêtre Tkinter
window.mainloop()
