import tkinter

# Créer une fenêtre Tkinter
window = tkinter.Tk()

# Créer un canevas Tkinter
canvas = tkinter.Canvas(window, width=500, height=500)
canvas.pack()

# Dessiner du texte
text = canvas.create_text(250, 250, text="Hello, world!")

# Afficher la fenêtre Tkinter
window.mainloop()
