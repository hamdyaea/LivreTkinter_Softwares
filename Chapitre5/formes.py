import tkinter

# Créer une fenêtre Tkinter
window = tkinter.Tk()

# Créer un canevas Tkinter
canvas = tkinter.Canvas(window, width=500, height=500)
canvas.pack()

# Dessiner une ligne
line = canvas.create_line(0, 0, 500, 500)

# Dessiner un rectangle
rectangle = canvas.create_rectangle(50, 50, 250, 250)

# Dessiner un cercle
circle = canvas.create_oval(100, 100, 200, 200)

# Dessiner un polygone
polygon = canvas.create_polygon(300, 300, 400, 400, 450, 350)

# Afficher la fenêtre Tkinter
window.mainloop()
