import tkinter as tk
from PIL import Image, ImageTk
# pip install pillow

root = tk.Tk()

# Charger l'image
image = Image.open("python.png")

# Créer un objet PhotoImage à partir de l'image
photo = ImageTk.PhotoImage(image)

# Afficher l'image dans un widget Canvas
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.create_image(0, 0, anchor=tk.NW, image=photo)
canvas.pack()

root.mainloop()
