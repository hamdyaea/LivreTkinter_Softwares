import tkinter as tk

def key_pressed(event):
    print("La touche", event.keysym, "a été enfoncée.")

root = tk.Tk()

root.bind("<Key>", key_pressed)

root.mainloop()
